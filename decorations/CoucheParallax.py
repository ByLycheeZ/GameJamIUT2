import pygame
from gestionnaires.Affichage import *
from interfaces.Ecran import Ecran


class CoucheParallax:
    def __init__(self, nb, vitesse, opacite=1.0):
        self.__image = pygame.image.load(f'res/img/parallax/{nb}.png').convert_alpha()
        self.__image.fill((255, 255, 255, int(opacite * 255)), None, pygame.BLEND_RGBA_MULT)
        self.__vitesse = vitesse

        self.__x_liste = [0]
        while self.__x_liste[-1] < Ecran.largeur + self.__image.get_width() * 2:
            self.__x_liste.append(len(self.__x_liste) * self.__image.get_width())

        Affichage().enregistrer(self, -nb)

    def affichage(self, ecran):
        for x in self.__x_liste:
            ecran.blit_absolu(self.__image, (x, 0))

    """
    :param direction La direction dans laquelle le personnage se déplace (1 : droite, -1 : gauche)
    """
    def deplacement(self, direction, delta):
        self.__x_liste = [x - direction * delta * self.__vitesse for x in self.__x_liste]

        largeur = self.__image.get_width()
        if self.__x_liste[0] < -largeur:
            self.__x_liste.append(len(self.__x_liste) * largeur + self.__x_liste.pop(0))

    def fin(self):
        Affichage().supprimer(self)
