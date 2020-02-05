from entites.Joueur import Joueur
from decorations.Parallax import Parallax
from utils.Constantes import TOUCHES
from interfaces.Ecran import Ecran
from interfaces.GameOver import GameOver
from gestionnaires.Maj import Maj



class Jeu:
    class __Jeu:
        def __init__(self, couleurs_joueurs):
            self.__joueurs = []
            for i in range(0, len(couleurs_joueurs)):
                self.__joueurs.append(Joueur(TOUCHES[i], couleurs_joueurs[i]))

            Maj().enregistrer(self)
            self.__parallax = Parallax()

        def fin(self):
            for joueur in self.__joueurs:
                joueur.fin()

            self.__parallax.fin()

        def maj(self, delta):
            mouvement = [0, 0]
            #for joueur in self.__joueurs:
                #mouvement += map.collision(joueur)  # sujet a des changement de nom et d'appel
                #il manque le deplacement effectif du joueur

    __instance = None
    __konami = False

    def __init__(self, couleurs_joueurs=None):
        if not Jeu.__instance and couleurs_joueurs:
            Jeu.__instance = Jeu.__Jeu(couleurs_joueurs)

    def fin(self, couleur):
        self.__instance.fin()
        Ecran.reinitialiser()
        GameOver(couleur)

    @staticmethod
    def konami():
        Jeu.__konami = True

    @staticmethod
    def konami_actif():
        return Jeu.__konami


