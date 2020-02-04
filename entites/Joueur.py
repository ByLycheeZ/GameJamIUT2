import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from gestionnaires.Evenement import *
from utils.Animation import Animation
from utils.Constantes import *
from decorations.Parallax import Parallax
from interfaces.Ecran import Ecran


class Joueur:
    TAILLE_IMAGE = [120, 120]
    CHEMIN_SPRITE = 'res/img/'
    NB_SAUT_MAX = 1

    def __init__(self):
        self.sprite = pygame.image.load(self.CHEMIN_SPRITE + 'dino-jaune.png')
        self.rect = self.sprite.get_rect()
        self.rect.y = HEIGHT - self.TAILLE_IMAGE[1]
        self.vitesse = 300
        self.deplacement = [0, 0]
        self.velocite_saut, self.vitesse_chute = 2, 4
        self.nb_saut_restant = 1

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
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_q:
                self.deplacement[0] -= 1
            elif evenement.key == pygame.K_d:
                self.deplacement[0] += 1
            elif evenement.key == pygame.K_SPACE and self.nb_saut_restant > 0:
                self.deplacement[1] -= self.velocite_saut
                self.nb_saut_restant -= 1

        else:  # KEYUP
            if evenement.key == pygame.K_q:
                self.deplacement[0] += 1
            elif evenement.key == pygame.K_d:
                self.deplacement[0] -= 1

        if self.deplacement[0] != 0:
            self.anim_active = self.anim_deplacement
        else:
            self.anim_active = self.anim_attente

    def maj(self, delta):
        self.anim_active.ajouter_temps(delta)
        self.rect = self.rect.move(self.vitesse * self.deplacement[0] * delta,
                                   self.vitesse * self.deplacement[1] * delta)

        self.deplacement[1] += self.vitesse_chute * delta
        # temporaire ne peut pas tomber dans le vide
        if self.rect.y >= 768 - 120:
            self.rect.y = 768 - 120
            self.deplacement[1] = 0
            self.ajout_saut()

        droite = self.rect.left + self.TAILLE_IMAGE[0]
        if Ecran.get_droite() - droite < 10:
            Ecran.deplacement(droite - Ecran.largeur + 10, Ecran.y)

        Parallax().deplacement_joueur(self.deplacement[0], delta)

    def affichage(self, ecran):
        sous_sprite = self.sprite.subsurface(self.anim_active.recuperer_image())
        sous_sprite_rect = sous_sprite.get_rect()
        sous_sprite_rect.x, sous_sprite_rect.y = self.rect.x, self.rect.y
        ecran.blit(pygame.transform.flip(sous_sprite, self.deplacement[0] < 0, False), sous_sprite_rect)

    def get_vitesse(self):
        return self.vitesse

    def get_sprite(self):
        return self.sprite

    def get_rect(self):
        return self.rect

    def get_deplacement(self):
        return self.deplacement

    def get_nb_saut_restant(self):
        return self.nb_saut_restant

    def get_nb_saut_max(self):
        return self.NB_SAUT_MAX

    def set_vitesse(self, vitesse):
        self.vitesse = vitesse

    def set_sprite(self, nom_fichier):
        self.sprite = pygame.image.load(self.CHEMIN_SPRITE + nom_fichier)

    def set_rect(self, rect):
        self.rect = rect

    def set_velocite_saut(self, velocite_saut):
        self.velocite_saut = velocite_saut

    def set_vitesse_chute(self, vitesse_chute):
        self.vitesse_chute = vitesse_chute

    def ajout_saut(self, nb=1):
        self.nb_saut_restant = min([nb + self.nb_saut_restant, self.NB_SAUT_MAX])

