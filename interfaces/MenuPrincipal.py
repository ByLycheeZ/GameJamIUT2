import pygame

from interfaces.elements.BoutonCredits import BoutonCredits
from interfaces.elements.BoutonJouer import BoutonJouer
from interfaces.elements.BoutonQuitter import BoutonQuitter


class MenuPrincipal:
    def __init__(self, ecran):
        self.background = pygame.image.load("res/accueil-background.png")
        self.titre = pygame.image.load("res/titre.png")
        self.bouton_jouer = BoutonJouer((350, 400), "bouton-jouer", self)
        self.bouton_quitter = BoutonQuitter((350, 500), "bouton-quitter", self)
        self.bouton_credits = BoutonCredits((910, 730), "bouton-credits", self)
        self.montrer_menu = True
        self.jouer = False
        self.credits = False
        # self.creditsImg = pygame.image.load("res/credits.png")

    def afficher(self, ecran):
        if not self.jouer and not self.credits:
            ecran.blit(self.background, (-490, 0))
            ecran.blit(self.titre, (80, 60))
            self.bouton_jouer.afficher(ecran)
            self.bouton_quitter.afficher(ecran)
            self.bouton_credits.afficher(ecran)
        elif self.credits:
            ecran.fill((0, 0, 0))
            # ecran.blit(self.creditsImg, (200, 300))
