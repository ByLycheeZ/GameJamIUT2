import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from gestionnaires.Evenement import *
from gestionnaires.Sons import Sons
from utils.Animation import Animation
from decorations.Parallax import Parallax
from interfaces.Ecran import Ecran


class Joueur:
    TAILLE_IMAGE = [24 * 5, 24 * 5]

    def __init__(self):
        self.sprite = pygame.image.load('res/img/dino-jaune.png')
        self.rect = self.sprite.get_rect()
        self.__vies = 5
        self.vitesse = 300
        self.deplacement = [0, 0]

        self.anim_attente = Animation(0, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.anim_deplacement = Animation(4, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)
        self.anim_attaque = Animation(10, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 3, 0.2)
        self.anim_degat = Animation(13, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.anim_accroupi = Animation(18, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)
        self.anim_active = self.anim_attente

        evenement = Evenement()
        evenement.enregistrer(pygame.KEYDOWN, self)
        evenement.enregistrer(pygame.KEYUP, self)
        Affichage().enregistrer(self, 1)
        Maj().enregistrer(self)

    def evenement(self, evenement):
        if self.__vies <= 0:
            return

        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_q:
                self.deplacement[0] -= 1
            elif evenement.key == pygame.K_d:
                self.deplacement[0] += 1

        else:  # KEYUP
            if evenement.key == pygame.K_q:
                self.deplacement[0] += 1
            elif evenement.key == pygame.K_d:
                self.deplacement[0] -= 1

        if self.deplacement[0] != 0 or self.deplacement[1] != 0:
            self.anim_active = self.anim_deplacement
        else:
            self.anim_active = self.anim_attente

    def maj(self, delta):
        if self.__vies <= 0:
            return

        self.anim_active.ajouter_temps(delta)
        self.rect = self.rect.move(self.vitesse * self.deplacement[0] * delta,
                                   self.vitesse * self.deplacement[1] * delta)

        self.maj_camera()
        Parallax().deplacement_joueur(self.deplacement[0], delta)

    def maj_camera(self):
        droite = self.rect.left + self.TAILLE_IMAGE[0]
        if Ecran.get_droite() - droite < 10:
            Ecran.deplacement(droite - Ecran.largeur + 10, Ecran.y)

        if Ecran.x > droite:
            self.retirer_vie()
            print(f'Il reste {self.__vies} vie(s)')

    def retirer_vie(self):
        self.__vies -= 1
        Sons().jouer_son('mort')
        if self.__vies > 0:
            self.revivre()
        else:
            self.mourir()

    def revivre(self):
        self.rect.x = Ecran.x + Ecran.largeur / 2

    def mourir(self):
        pass

    def affichage(self, ecran):
        if self.__vies <= 0:
            return

        sous_sprite = self.sprite.subsurface(self.anim_active.recuperer_image())
        sous_sprite_rect = sous_sprite.get_rect()
        sous_sprite_rect.x, sous_sprite_rect.y = self.rect.x, self.rect.y
        ecran.blit(pygame.transform.flip(sous_sprite, self.deplacement[0] < 0, False), sous_sprite_rect)
