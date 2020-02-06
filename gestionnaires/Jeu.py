from entites.Joueur import Joueur
from entites.JoueurTornade import JoueurTornade
from decorations.Parallax import Parallax
from gestionnaires.Carte import Carte
from utils.Constantes import TOUCHES
from interfaces.Ecran import Ecran
from interfaces.GameOver import GameOver


class Jeu:
    class __Jeu:
        def __init__(self, couleurs_joueurs):
            self.__joueurs = []
            for i in range(0, len(couleurs_joueurs)):
                self.__joueurs.append(JoueurTornade(TOUCHES[i], couleurs_joueurs[i]))

            self.__parallax = Parallax()
            self.__carte = Carte()

        def fin(self):
            for joueur in self.__joueurs:
                joueur.fin()

            self.__parallax.fin()
            self.__carte.fin()

        def collisions(self, joueur, delta):
            return self.__carte.collisions(joueur, delta)

        def get_joueurs(self):
            return self.__joueurs

    __instance = None
    __konami = False

    def __init__(self, couleurs_joueurs=None):
        if not Jeu.__instance and couleurs_joueurs:
            Jeu.__instance = Jeu.__Jeu(couleurs_joueurs)

    def fin(self, couleur):
        self.__instance.fin()
        Ecran.reinitialiser()
        GameOver(couleur)
        Jeu.__instance = None

    def collisions(self, joueur, delta):
        return self.__instance.collisions(joueur, delta)

    def get_joueurs(self):
        return self.__instance.get_joueurs()

    @staticmethod
    def konami():
        Jeu.__konami = True

    @staticmethod
    def konami_actif():
        return Jeu.__konami
