import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement

from interfaces.elements.BoutonRetourAccueil import BoutonRetourAccueil


class Pause:
    BACKGROUND = (99, 110, 114, 128)  # Gris foncé transparent

    def __init__(self, jeu):
        self.montrer = True
        self.__bg = pygame.image.load("res/img/interfaces/accueil/accueil-background.png")
        self.__jeu = jeu
        self.__bouton_retour = BoutonRetourAccueil((350, 450), "bouton-retour-accueil", self)
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.__bg, (-490, 0))
            ecran.fill(self.BACKGROUND, None, pygame.BLEND_RGBA_MULT)
            self.__bouton_retour.affichage(ecran)

    def evenement(self, evenement):
        if self.montrer:
            if evenement.key == pygame.K_ESCAPE or evenement.key == pygame.K_p:
                self.montrer = False

