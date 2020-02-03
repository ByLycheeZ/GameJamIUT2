import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from utils.Animation import Animation


class Joueur:
    TAILLE_IMAGE = [24 * 5, 24 * 5]

    def __init__(self):
        self.sprite = pygame.image.load('res/img/dino-jaune.png')
        self.anim_attente = Animation(0, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.anim_deplacement = Animation(4, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)
        self.anim_attaque = Animation(10, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 3, 0.2)
        self.anim_degat = Animation(13, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.anim_accroupi = Animation(18, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)

        Affichage().enregistrer(self)
        Maj().enregistrer(self)

    def maj(self, delta):
        self.anim_accroupi.ajouter_temps(delta)

    def affichage(self, ecran):
        ecran.blit(self.sprite, self.sprite.get_rect(), self.anim_accroupi.recuperer_image())
