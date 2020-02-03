import pygame

from interfaces.elements.BoutonJouer import BoutonJouer
from interfaces.elements.BoutonQuitter import BoutonQuitter

from gestionnaires.Evenement import *


class MenuPrincipal:
    def __init__(self, ecran):
        self.background = pygame.image.load("res/accueil-background.png")
        self.title = "Windy Course"
        self.bouton_jouer = BoutonJouer("Jouer", (350, 400))
        self.bouton_quitter = BoutonQuitter("Quitter", (350, 500))
        # self.credits = BoutonCredits()
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def afficher(self, ecran):
        ecran.blit(self.background, (-490, 0))
        self.bouton_jouer.afficher(ecran)
        self.bouton_quitter.afficher(ecran)

    def evenement(self, evenement):
        if (self.bouton_jouer.coord[0] <= pygame.mouse.get_pos()[0] <= self.bouton_jouer.coord[0] + 300) \
                and (self.bouton_jouer.coord[1] <= pygame.mouse.get_pos()[1] <= self.bouton_jouer.coord[1] + 76):
            print("Jouer")
        elif (self.bouton_quitter.coord[0] <= pygame.mouse.get_pos()[0] <= self.bouton_quitter.coord[0] + 300) \
                and (self.bouton_quitter.coord[1] <= pygame.mouse.get_pos()[1] <= self.bouton_quitter.coord[1] + 76):
            quit()
