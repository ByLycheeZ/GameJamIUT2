import pygame

from gestionnaires.Affichage import Affichage

from interfaces.Credits import Credits

from interfaces.elements.BoutonCredits import BoutonCredits
from interfaces.elements.BoutonJouer import BoutonJouer
from interfaces.elements.BoutonQuitter import BoutonQuitter


class MenuPrincipal:
    def __init__(self):
        self.background = pygame.image.load("res/img/accueil-background.png")
        self.titre = pygame.image.load("res/img/titre.png")
        self.bouton_jouer = BoutonJouer((350, 400), "bouton-jouer", self)
        self.bouton_quitter = BoutonQuitter((350, 500), "bouton-quitter", self)
        self.bouton_credits = BoutonCredits((910, 730), "bouton-credits", self)
        self.montrer = True
        self.credits = Credits(self)
        Affichage().enregistrer(self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.background, (-490, 0))
            ecran.blit(self.titre, (80, 60))
            self.bouton_jouer.affichage(ecran)
            self.bouton_quitter.affichage(ecran)
            self.bouton_credits.affichage(ecran)


