import pygame

from gestionnaires.Evenement import Evenement
from gestionnaires.Affichage import Affichage
from utils.Constantes import LARGEUR


class BoutonRejouer:
    def __init__(self, parent, y):
        font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 70)
        self.__parent = parent
        self.__texte = font.render('Rejouer', True, (255, 255, 255))
        self.__coord = ((LARGEUR / 2) - (self.__texte.get_width() / 2), y)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)
        Affichage().enregistrer(self, 3)

    def evenement(self, evenement):
        from interfaces.MenuPrincipal import MenuPrincipal
        if (self.__coord[0] <= pygame.mouse.get_pos()[0] <= self.__coord[0] + 300) \
                and (self.__coord[1] <= pygame.mouse.get_pos()[1] <= self.__coord[1] + 76):
            Evenement().supprimer(self)
            Affichage().supprimer(self)
            self.__parent.fin()
            MenuPrincipal()

    def affichage(self, ecran):
        ecran.blit_absolu(self.__texte, self.__coord)
