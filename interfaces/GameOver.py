from random import random

import pygame

from gestionnaires.Sons import Sons
from interfaces.elements.FinJeu import FinJeu
from utils.Animation import Animation
from utils.Constantes import COULEURS, HAUTEUR, TAILLE_PERSO
from entites.Dino import Dino
from gestionnaires.Affichage import Affichage
from gestionnaires.Maj import Maj


class GameOver:
    FOND = (0, 0, 0)

    def __init__(self, couleur):
        liste_couleurs = COULEURS.copy()
        liste_couleurs.remove(couleur)

        x = -TAILLE_PERSO[0]
        y = HAUTEUR / 2 - TAILLE_PERSO[1] / 2
        self.__vainqueur = Dino(couleur, (x, y), (1, 0))
        x -= 50
        self.__perdants = []
        for coul in liste_couleurs:
            x -= random() * 100 + TAILLE_PERSO[0] * 0.5
            self.__perdants.append(Dino(coul, (x, y), (1, 0)))

        self.__temps_anim = 0
        self.__fin_jeu = FinJeu(couleur, TAILLE_PERSO[1] + y)

        Affichage().enregistrer(self, -1)
        Maj().enregistrer(self)

    def affichage(self, ecran):
        ecran.fill(self.FOND)

    def maj(self, delta):
        self.__temps_anim += delta

        if not self.__fin_jeu.debut and self.__vainqueur.get_pos()[0] >= 700:
            self.__fin_jeu.debut = True

        if self.__fin_jeu.fin:
            self.__vainqueur.deplacement = (-1, 0)
            self.__vainqueur.vitesse = 0
            self.__vainqueur.anim = Animation(0, 0, TAILLE_PERSO[0], TAILLE_PERSO[1], 4, 0.2)

            for dino in self.__perdants:
                dino.fin()

            sons = Sons()
            from gestionnaires.Jeu import Jeu
            if Jeu.konami_actif():
                sons.jouer_son('k-mort2')
            else:
                sons.jouer_son('mort')
                sons.jouer_son('mort2')
                sons.jouer_son('mort3')

            sons.jouer_son('crash', 'ogg')

            Maj().supprimer(self)
