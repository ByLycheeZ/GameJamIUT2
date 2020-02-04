import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from gestionnaires.Evenement import *
from gestionnaires.Sons import Sons
import gestionnaires.Jeu as Jeu
from utils.Animation import Animation
from utils.Constantes import *
from decorations.Parallax import Parallax
from interfaces.Ecran import Ecran
from interfaces.hud.HudVie import HudVie


class Joueur:
    TAILLE_IMAGE = [120, 120]
    CHEMIN_SPRITE = 'res/img/'
    NB_SAUT_MAX = 1

    __count = 0

    def __init__(self, touches, couleur):
        Joueur.__count += 1
        self.__vies = 5
        self.__sprite = pygame.image.load(f'{self.CHEMIN_SPRITE}dino-{couleur}.png')
        self.__hud = HudVie(self.__vies, couleur)
        self.__couleur = couleur
        self.__rect = self.__sprite.get_rect()
        self.__rect.y = HAUTEUR - self.TAILLE_IMAGE[1]
        self.__vitesse = 300
        self.__deplacement = [0, 0]
        self.__velocite_saut, self.vitesse_chute = 2, 4
        self.__nb_saut_restant = 1
        self.__touches = touches

        self.__anim_attente = Animation(0, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.__anim_deplacement = Animation(4, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)
        self.__anim_attaque = Animation(10, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 3, 0.2)
        self.__anim_degat = Animation(13, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.__anim_accroupi = Animation(18, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)
        self.__anim_active = self.__anim_attente

        evenement = Evenement()
        evenement.enregistrer(pygame.KEYDOWN, self)
        evenement.enregistrer(pygame.KEYUP, self)
        Affichage().enregistrer(self, 1)
        Maj().enregistrer(self)

    def evenement(self, evenement):
        if self.__vies <= 0:
            return

        if evenement.type == pygame.KEYDOWN:
            if evenement.key == self.__touches.get('aller_gauche'):
                self.__deplacement[0] -= 1
            elif evenement.key == self.__touches.get('aller_droite'):
                self.__deplacement[0] += 1
            elif evenement.key == self.__touches.get('sauter') and self.__nb_saut_restant > 0:
                self.__deplacement[1] -= self.__velocite_saut
                self.__nb_saut_restant -= 1

        else:  # KEYUP
            if evenement.key == self.__touches.get('aller_gauche'):
                self.__deplacement[0] += 1
            elif evenement.key == self.__touches.get('aller_droite'):
                self.__deplacement[0] -= 1

        if self.__deplacement[0] != 0:
            self.__anim_active = self.__anim_deplacement
        else:
            self.__anim_active = self.__anim_attente

    def maj(self, delta):
        if self.__vies <= 0:
            return
        elif Joueur.__count == 1:
            jeu.Jeu().fin(self.__couleur)

        self.__anim_active.ajouter_temps(delta)
        self.__rect = self.__rect.move(self.__vitesse * self.__deplacement[0] * delta,
                                       self.__vitesse * self.__deplacement[1] * delta)

        self.__deplacement[1] += self.vitesse_chute * delta
        # temporaire ne peut pas tomber dans le vide
        if self.__rect.y >= 768 - 120:
            self.__rect.y = 768 - 120
            self.__deplacement[1] = 0
            self.ajout_saut()

        self.__maj_camera()
        Parallax().deplacement_joueur(self.__deplacement[0], delta)

    def __maj_camera(self):
        droite = self.__rect.left + self.TAILLE_IMAGE[0]
        if Ecran.get_droite() - droite < 10:
            Ecran.deplacement(droite - Ecran.largeur + 10, Ecran.y)

        if Ecran.x > droite:
            self.__retirer_vie()

    def __retirer_vie(self):
        self.__vies -= 1
        self.__hud.retirer_pv()
        Sons().jouer_son('mort')
        if self.__vies > 0:
            self.__revivre()
        else:
            Joueur.__count -= 1

    def __revivre(self):
        self.__rect.x = Ecran.x + Ecran.largeur / 2

    def affichage(self, ecran):
        if self.__vies <= 0:
            return

        sous_sprite = self.__sprite.subsurface(self.__anim_active.recuperer_image())
        sous_sprite_rect = sous_sprite.get_rect()
        sous_sprite_rect.x, sous_sprite_rect.y = self.__rect.x, self.__rect.y
        ecran.blit(pygame.transform.flip(sous_sprite, self.__deplacement[0] < 0, False), sous_sprite_rect)

    def get_vitesse(self):
        return self.__vitesse

    def get_sprite(self):
        return self.__sprite

    def get_rect(self):
        return self.__rect

    def get_deplacement(self):
        return self.__deplacement

    def get_nb_saut_restant(self):
        return self.__nb_saut_restant

    def get_nb_saut_max(self):
        return self.NB_SAUT_MAX

    def set_vitesse(self, vitesse):
        self.__vitesse = vitesse

    def set_sprite(self, nom_fichier):
        self.__sprite = pygame.image.load(self.CHEMIN_SPRITE + nom_fichier)

    def set_rect(self, rect):
        self.__rect = rect

    def set_velocite_saut(self, velocite_saut):
        self.__velocite_saut = velocite_saut

    def set_vitesse_chute(self, vitesse_chute):
        self.vitesse_chute = vitesse_chute

    def ajout_saut(self, nb=1):
        self.__nb_saut_restant = min([nb + self.__nb_saut_restant, self.NB_SAUT_MAX])

    def fin(self):
        self.__hud.fin()
        Evenement().supprimer(self)
        Affichage().supprimer(self)
        Maj().supprimer(self)

