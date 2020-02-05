import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement

from interfaces.elements.BoutonEquipe import BoutonEquipe
from interfaces.elements.BoutonSources import BoutonSources


class Credits:
    def __init__(self, menu):
        self.montrer = False
        self.equipe = True
        self.sources = False
        self.__textes = []
        self.__menu = menu
        self.__bouton_sources = BoutonSources((880, 730), "", self)
        self.__bouton_equipe = BoutonEquipe((10, 730), "", self)
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            background = pygame.image.load("res/img/interfaces/accueil/accueil-background.png")
            ecran.blit(background, (-490, 0))
            image = pygame.image.load("res/img/interfaces/selection/esc-message.png")
            ecran.blit(image, (320, 730))
            if self.equipe and not self.sources:
                image = pygame.image.load("res/img/interfaces/credits/credits.png")
            elif self.sources and not self.equipe:
                image = pygame.image.load("res/img/interfaces/credits/images-sons.png")
            else:
                image = pygame.image.load("res/img/interfaces/fin/fin-jeu.png")
            ecran.blit(image, (0, 0))

    def evenement(self, evenement):
        if self.montrer and evenement.key == pygame.K_ESCAPE:
            self.montrer = False
            self.equipe = True
            self.sources = False
            self.__menu.montrer = True
