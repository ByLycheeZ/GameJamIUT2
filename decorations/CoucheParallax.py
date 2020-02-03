import pygame
from gestionnaires.Affichage import *


class CoucheParallax:
    def __init__(self, nb, vitesse, opacite=1.0):
        self.__image = pygame.image.load(f'res/img/parallax/{nb}.png').convert_alpha()
        self.__image.fill((255, 255, 255, int(opacite * 255)), None, pygame.BLEND_RGBA_MULT)
        self.__vitesse = vitesse

        self.__x1 = 0
        self.__x2 = self.__image.get_width()

        Affichage().enregistrer(self)

    def affichage(self, ecran):
        ecran.blit(self.__image, (self.__x1, 0))
        ecran.blit(self.__image, (self.__x2, 0))

    """
    :param direction La direction dans laquelle le personnage se déplace (1 : droite, -1 : gauche)
    """
    def deplacement(self, direction, delta):
        # Le parallax background doit se déplacer à l'opposé du joueur pour paraître réaliste
        self.__x1 = self.__recup_pos(self.__x1, direction, delta)
        self.__x2 = self.__recup_pos(self.__x2, direction, delta)

    def __recup_pos(self, x, direction, delta):
        largeur = self.__image.get_width()
        x += -direction * self.__vitesse * delta
        if x < -largeur:
            x += 2 * largeur
        elif x > largeur:
            x -= 2 * largeur
        return x