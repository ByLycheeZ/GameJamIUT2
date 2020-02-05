import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Maj import Maj
from utils.Constantes import LARGEUR


class FinJeu:
    def __init__(self, couleur, y_fin):
        self.__texte = pygame.image.load(f'res/img/interfaces/victoire-{couleur}.png').convert_alpha()
        self.__rect_texte = self.__texte.get_rect()
        self.__rect_texte.x = LARGEUR / 2 - self.__rect_texte.width / 2
        self.__rect_texte.y = -self.__rect_texte.height * 2
        self.__vitesse = 500
        self.__y_fin = y_fin
        self.debut = False
        self.fin = False

        Affichage().enregistrer(self, 2)
        Maj().enregistrer(self)

    def affichage(self, ecran):
        ecran.blit(self.__texte, self.__rect_texte)

    def maj(self, delta):
        if self.debut:
            if self.__rect_texte.y + self.__rect_texte.height < self.__y_fin:
                self.__vitesse += 800 * delta
                self.__rect_texte = self.__rect_texte.move(0, delta * self.__vitesse)
            else:
                self.fin = True
                Maj().supprimer(self)
