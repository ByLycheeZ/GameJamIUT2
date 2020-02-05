from entites.Joueur import Joueur
from entites.Tornade import Tornade
from decorations.Parallax import Parallax
from utils.Constantes import TOUCHES
from interfaces.Ecran import Ecran
from interfaces.GameOver import GameOver


class Jeu:
    class __Jeu:
        def __init__(self, couleurs_joueurs):
            self.__joueurs = []
            for i in range(0, len(couleurs_joueurs)):
                self.__joueurs.append(Joueur(TOUCHES[i], couleurs_joueurs[i]))
            Tornade([0, 350], [1, 0])
            self.__parallax = Parallax()

        def fin(self):
            for joueur in self.__joueurs:
                joueur.fin()

            self.__parallax.fin()

    __instance = None

    def __init__(self, couleurs_joueurs=None):
        if not Jeu.__instance and couleurs_joueurs:
            Jeu.__instance = Jeu.__Jeu(couleurs_joueurs)

    def fin(self, couleur):
        self.__instance.fin()
        Ecran.reinitialiser()
        GameOver(couleur)
