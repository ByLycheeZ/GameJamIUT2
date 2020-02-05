import pygame

from gestionnaires.Affichage import Affichage

from interfaces.ChoixPersonnages import ChoixPersonnages
from interfaces.Credits import Credits

from interfaces.elements.BoutonCredits import BoutonCredits
from interfaces.elements.BoutonJouer import BoutonJouer
from interfaces.elements.BoutonQuitter import BoutonQuitter


class MenuPrincipal:
    def __init__(self):
        self.montrer = True
        self.credits = Credits(self)
        self.choix_personnages = ChoixPersonnages(self)
        self.__background = pygame.image.load("res/img/interfaces/accueil/accueil-background.png")
        self.__titre = pygame.image.load("res/img/interfaces/accueil/titre.png")
        self.__bouton_jouer = BoutonJouer((350, 400), "bouton-jouer", self)
        self.__bouton_quitter = BoutonQuitter((350, 500), "bouton-quitter", self)
        self.__bouton_credits = BoutonCredits((910, 730), "bouton-credits", self)
        Affichage().enregistrer(self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.__background, (-490, 0))
            ecran.blit(self.__titre, (80, 60))
            self.__bouton_jouer.affichage(ecran)
            self.__bouton_quitter.affichage(ecran)
            self.__bouton_credits.affichage(ecran)
