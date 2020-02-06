import pygame
from entites.Joueur import Joueur
from entites.JoueurTornade import JoueurTornade
from decorations.Parallax import Parallax
from gestionnaires.Carte import Carte
from gestionnaires.Evenement import Evenement
from gestionnaires.Maj import Maj
from interfaces.Pause import Pause
from utils.Constantes import TOUCHES
from interfaces.Ecran import Ecran
from interfaces.GameOver import GameOver
from gestionnaires.Sons import Sons


class Jeu:
    class __Jeu:
        def __init__(self, couleurs_joueurs):
            self.__joueurs = []
            for i in range(0, len(couleurs_joueurs)):
                self.__joueurs.append(JoueurTornade(TOUCHES[i], couleurs_joueurs[i]))

            self.__parallax = Parallax()
            self.__carte = Carte()
            if Jeu().konami_actif():
                Sons().jouer_musique('fond-konami')
            else:
                Sons().jouer_musique('fond')


            Evenement().enregistrer(pygame.KEYUP, self)
            self.__pause = Pause()

        def fin(self):
            for joueur in self.__joueurs:
                joueur.fin()

            self.__parallax.fin()
            self.__carte.fin()
            if Jeu().konami_actif():
                Sons().pause_musique('fond-konami')
            else:
                Sons().pause_musique('fond')

        def evenement(self, evenement):
            if evenement.key == pygame.K_p or evenement.key == pygame.K_ESCAPE:
                self.__pause.montrer = not self.__pause.montrer
                Evenement().pause(self.__pause)
                Maj().pause(self.__pause)

        def collisions(self, joueur, delta):
            return self.__carte.collisions(joueur, delta)

        def get_joueurs(self):
            return self.__joueurs

    __instance = None
    __konami = False

    def __init__(self, couleurs_joueurs=None):
        if not Jeu.__instance and couleurs_joueurs:
            Jeu.__instance = Jeu.__Jeu(couleurs_joueurs)

    def fin(self, couleur=None):
        self.__instance.fin()
        Ecran.reinitialiser()
        if couleur:
            GameOver(couleur)
        Jeu.__instance = None

    def collisions(self, joueur, delta):
        return self.__instance.collisions(joueur, delta)

    def get_joueurs(self):
        if self.__instance:
            return self.__instance.get_joueurs()
        return None

    @staticmethod
    def konami():
        Jeu.__konami = True

    @staticmethod
    def konami_actif():
        return Jeu.__konami
