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
            for joueur in self.__joueurs:
                #mouvement[0], mouvement[1] += map.collision(joueur, delta)  # sujet a des changement de nom et d'appel  # le delta sert pour le mouvement du courant
                #il manque le deplacement effectif du joueur
                if mouvement[1] != 0:
                    joueur.set_vitesse([joueur.get_vitesse()[0], 0])
                joueur.set_rect(joueur.get_rect().move(joueur.get_vitesse() * joueur.get_deplacement()[0] * delta * max(mouvement[0], -1),
                                                       joueur.get_vitesse() * joueur.get_deplacement()[1] * delta * max(mouvement[1], -1)))


    __instance = None

    def __init__(self, couleurs_joueurs=None):
        if not Jeu.__instance and couleurs_joueurs:
            Jeu.__instance = Jeu.__Jeu(couleurs_joueurs)

    def fin(self, couleur):
        self.__instance.fin()
        Ecran.reinitialiser()
        GameOver(couleur)




