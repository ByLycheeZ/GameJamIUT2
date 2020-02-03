import pygame
from gestionnaires.Affichage import *


class Ecran(pygame.Surface):
    decalage = pygame.Vector2()
    x, y = 0, 0
    largeur, hauteur = None, None

    def __init__(self, ecran):
        if not Ecran.largeur and not Ecran.hauteur:
            Ecran.largeur, Ecran.hauteur = ecran.get_width(), ecran.get_height()
            super(Ecran, self).__init__((Ecran.largeur, Ecran.hauteur))
            self.__affichage = Affichage()
        else:
            raise RuntimeError('Un écran a déjà été créé.')

    @staticmethod
    def deplacement(x, y):
        Ecran.x, Ecran.y = x, y

    @staticmethod
    def get_droite():
        return Ecran.x + Ecran.largeur

    @staticmethod
    def get_bas():
        return Ecran.y + Ecran.hauteur

    def affichage(self, ecran):
        self.__affichage.maj(self)
        ecran.blit(self, (0, 0))

    def blit(self, source, dest, area=None, special_flags=0):
        new_dest = (dest[0] - Ecran.x, dest[1] - Ecran.y)
        super(Ecran, self).blit(source, new_dest, area, special_flags)