import pygame
from utils.Animation import Animation
from utils.Constantes import CHEMIN_SPRITE, TAILLE_PERSO
from gestionnaires.Maj import Maj
from gestionnaires.Affichage import Affichage


class Dino:
    def __init__(self, couleur, position, deplacement):
        self.__sprite = pygame.image.load(f'{CHEMIN_SPRITE}dino-{couleur}.png')
        self.__rect = self.__sprite.get_rect()
        self.__rect.x, self.__rect.y = position
        self.vitesse = 300
        self.deplacement = deplacement

        self.anim = Animation(18, 0, TAILLE_PERSO[0], TAILLE_PERSO[1], 6, 0.2)

        Maj().enregistrer(self)
        Affichage().enregistrer(self)

    def maj(self, delta):
        self.anim.ajouter_temps(delta)
        self.__rect = self.__rect.move(self.vitesse * self.deplacement[0] * delta,
                                       self.vitesse * self.deplacement[1] * delta)

    def affichage(self, ecran):
        sous_sprite, sous_sprite_rect = self.anim.recuperer_sous_sprite(self.__sprite, self.__rect.x, self.__rect.y)
        ecran.blit(pygame.transform.flip(sous_sprite, self.deplacement[0] < 0, False), sous_sprite_rect)

    def get_pos(self):
        return self.__rect.x, self.__rect.y

    def fin(self):
        Affichage().supprimer(self)
        Maj().supprimer(self)