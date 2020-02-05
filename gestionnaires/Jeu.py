from entites.Joueur import Joueur
from decorations.Parallax import Parallax
from gestionnaires.Carte import Carte
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
            self.__carte = Carte()

        def fin(self):
            for joueur in self.__joueurs:
                joueur.fin()

            self.__parallax.fin()
            self.__carte.fin()

        def maj(self, delta):
            for joueur in self.__joueurs:
                collision = self.__carte.collisions(joueur, delta)

                if collision:
                    d = joueur.get_deplacement()
                    rect = joueur.get_rect()
                    if d[1] > 0:
                        rect.bottom = collision.top
                        joueur.set_deplacement([joueur.get_deplacement()[0], 0])
                        joueur.ajout_saut(1)
                    elif d[0] < 0:
                        rect.left = collision.right
                    elif d[0] > 0:
                        rect.right = collision.left
                    elif d[1] < 0:
                        rect.top = collision.bottom
                    joueur.set_rect(rect)

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

    @staticmethod
    def konami():
        Jeu.__konami = True

    @staticmethod
    def konami_actif():
        return Jeu.__konami
