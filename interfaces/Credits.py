import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement
from gestionnaires.Maj import Maj


class Credits:
    def __init__(self, menu):
        self.montrer = False
        self.__textes = []
        self.__coord = (400, 810)
        self.__menu = menu
        Affichage().enregistrer(self)
        Maj().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.fill((45, 52, 54))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 40)
            self.__textes.append("Léo Le Corre")
            for credit in self.__textes:
                texte = font.render(credit, False, (255, 255, 255))
                ecran.blit(texte, (self.__coord[0], self.__coord[1]))

    def maj(self, delta):
        self.__coord = (400, self.__coord[1] - 50 * delta)
        if self.__coord[1] <= -300:
            self.montrer = False
            #self.__menu.montrer = True
            self.__coord = (400, 810)

    def evenement(self, evenement):
        if evenement.key == pygame.K_ESCAPE:
            self.montrer = False
            self.__menu.montrer = True
            self.__coord = (400, 810)
