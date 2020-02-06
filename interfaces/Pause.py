import pygame

import interfaces.MenuPrincipal as MenuPrincipal
import gestionnaires.Jeu as Jeu

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement
from interfaces.Ecran import Ecran

from interfaces.elements.BoutonRetourAccueil import BoutonRetourAccueil
from interfaces.elements.BoutonRetourJeu import BoutonRetourJeu
from utils import Constantes


class Pause:
    BACKGROUND = (99, 110, 114, 128)  # Gris transparent
    RETOUR = (255, 255, 255)  # Blanc
    MENU = (231, 76, 60)  # Rouge
    MESSAGE = (255, 255, 255)  # Blanc

    def __init__(self):
        self.montrer = False
        self.__jeu = Jeu.Jeu()
        self.__bouton_retour_jeu = BoutonRetourJeu((Constantes.LARGEUR/2 - 212, 300), "", self)
        self.__bouton_retour_accueil = BoutonRetourAccueil((Constantes.LARGEUR/2 - 300, 460), "", self)
        Affichage().enregistrer(self, 2)

    def affichage(self, ecran):
        if self.montrer:
            ecran.fill(self.BACKGROUND, None, pygame.BLEND_RGBA_MULT)
            self.__bouton_retour_jeu.affichage(ecran)
            self.__bouton_retour_accueil.affichage(ecran)
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 60)
            texte = font.render("Retour au jeu", True, self.RETOUR)
            ecran.blit(texte, (Constantes.LARGEUR/2 - texte.get_width()/2, 300))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 40)
            texte = font.render("Quitter la partie", True, self.MENU)
            ecran.blit(texte, (Constantes.LARGEUR/2 - texte.get_width()/2, 460))

    def fin(self):
        self.__jeu.fin()
        Ecran.reinitialiser()
        MenuPrincipal.MenuPrincipal()
        self.__jeu = None
        Affichage().supprimer(self)
        Evenement().supprimer(self.__bouton_retour_accueil)
        Evenement().supprimer(self.__bouton_retour_jeu)
