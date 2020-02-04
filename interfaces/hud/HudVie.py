import pygame
from gestionnaires.Affichage import Affichage
from utils.Constantes import COUCHE_HUD, WIDTH, HEIGHT


class HudVie:
    MARGE_EXTERIEURE = 10
    MARGE_INTERIEURE = 2
    __compte = 0

    def __init__(self, pv, couleur):
        self.__max_pv = pv
        self.__pv = pv
        self.__coeur = pygame.image.load(f'res/img/hud/coeur-{couleur}.bmp')
        self.__coeur_vide = pygame.image.load('res/img/hud/coeur_perdu.bmp')

        self.__init__position()
        HudVie.__compte += 1

        Affichage().enregistrer(self, COUCHE_HUD)

    def __init__position(self):
        self.__x = self.MARGE_EXTERIEURE if self.__compte % 2 == 0 \
                   else WIDTH - self.MARGE_EXTERIEURE - self.__max_pv * (self.MARGE_INTERIEURE + self.__coeur.get_width())

        self.__y = self.MARGE_EXTERIEURE if self.__compte < 2 \
                   else HEIGHT - self.MARGE_EXTERIEURE - self.__coeur.get_height()

    def retirer_pv(self):
        self.__pv -= 1

    def gagner_pv(self):
        self.__pv = min((self.__pv + 1, self.__max_pv))

    def affichage(self, ecran):
        for i in range(1, self.__max_pv + 1):
            x = self.__x + (self.__coeur.get_width() + self.MARGE_INTERIEURE) * (i - 1)
            if self.__pv >= i:
                ecran.blit_absolu(self.__coeur, (x, self.__y))
            else:
                ecran.blit_absolu(self.__coeur_vide, (x, self.__y))
