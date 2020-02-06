import pygame
import math
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from gestionnaires.Sons import Sons
from utils.Animation import Animation


class Tornade:
    TAILLE_IMAGE = [64, 64]
    CHEMIN_SPRITE = 'res/img/competences/'

    def __init__(self, positions, deplacement, couleur_joueur, vitesse=400, duree=3):
        self.__couleur_joueur = couleur_joueur
        self.__temps_fin = pygame.time.get_ticks() / 1000 + duree
        self.__sprite = pygame.image.load(self.CHEMIN_SPRITE + 'Tornade.png')
        self.__rect = self.__sprite.get_rect()
        self.__rect.x, self.__rect.y = positions
        self.__deplacement = deplacement
        self.__vitesse = vitesse
        self.__animimation = Animation(0, 0, Tornade.TAILLE_IMAGE[0], Tornade.TAILLE_IMAGE[1], 4, duree/12)

        Sons().jouer_son('Tornade', 'wav', math.ceil(duree/3) - 1, duree)  # Avec 3 la duree du sons
        Affichage().enregistrer(self, 1)
        Maj().enregistrer(self)

    def maj(self, delta):
        if pygame.time.get_ticks() / 1000 <= self.__temps_fin:
            self.__animimation.ajouter_temps(delta)
            self.__rect = self.__rect.move(self.__vitesse * self.__deplacement[0] * delta,
                                           self.__vitesse * self.__deplacement[1] * delta)
        else:
            Maj().supprimer(self)

    def affichage(self, ecran):
        if pygame.time.get_ticks() / 1000 <= self.__temps_fin:
            sous_sprite = self.__sprite.subsurface(self.__animimation.recuperer_image())
            sous_sprite_rect = sous_sprite.get_rect()
            sous_sprite_rect.x, sous_sprite_rect.y = self.__rect.x, self.__rect.y
            ecran.blit(pygame.transform.flip(sous_sprite, self.__deplacement[0] < 0, False), sous_sprite_rect)
        else:
            Affichage().supprimer(self)

    def set_deplacement(self, deplacement):
        self.__deplacement = deplacement

    def get_rect(self):
        return self.__rect

    def get_couleur_joueur(self):
        return self.__couleur_joueur

    def collisions(self, joueur, delta):
        this_rect = self._dessin.get_rect()
        this_rect.x, this_rect.y = self._x, self._y
        j_rect = joueur.get_rect_collision()
        return this_rect if this_rect.colliderect(j_rect) else None
