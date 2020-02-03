import pygame

from interfaces.elements.BoutonCredits import BoutonCredits
from interfaces.elements.BoutonJouer import BoutonJouer
from interfaces.elements.BoutonQuitter import BoutonQuitter


class MenuPrincipal:
    def __init__(self, ecran):
        self.background = pygame.image.load("res/accueil-background.png")
        self.title = "Windy Course"
        self.bouton_jouer = BoutonJouer("Jouer", (350, 400))
        self.bouton_quitter = BoutonQuitter("Quitter", (350, 500))
        self.bouton_credits = BoutonCredits("Credits", (910, 730))

    def afficher(self, ecran):
        ecran.blit(self.background, (-490, 0))
        self.bouton_jouer.afficher(ecran)
        self.bouton_quitter.afficher(ecran)
        self.bouton_credits.afficher(ecran)
