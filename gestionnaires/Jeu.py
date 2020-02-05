import pygame
from entites.Joueur import Joueur
from decorations.Parallax import Parallax
from gestionnaires.Carte import Carte
from gestionnaires.Evenement import Evenement
from interfaces.Pause import Pause
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

            Evenement().enregistrer(pygame.KEYUP, self)
            self.__pause = Pause(self)

        def fin(self):
            for joueur in self.__joueurs:
                joueur.fin()

            self.__parallax.fin()
            self.__carte.fin()

        def maj(self, delta):
            mouvement = [0, 0] #a retirer après implementation dans la map
            for joueur in self.__joueurs:
                #mouvement[0], mouvement[1] = map.collision(joueur, delta)  # sujet a des changement de nom et d'appel  # le delta sert pour le mouvement du courant
                #il manque le deplacement effectif du joueur
                #dans map : (max(mouvement[0], -1), max(mouvement[1], -1)

                if mouvement[1] != 0:
                    joueur.set_vitesse([joueur.get_vitesse()[0], 0])
                joueur.set_rect(joueur.get_rect().move(joueur.get_vitesse() * joueur.get_deplacement()[0] * delta * mouvement[0],
                                                       joueur.get_vitesse() * joueur.get_deplacement()[1] * delta * mouvement[1]))

        def evenement(self, evenement):
            if evenement.key == pygame.K_p:
                self.__pause.montrer = not self.__pause.montrer
            elif evenement.key == pygame.K_ESCAPE and self.__pause.montrer:
                self.__pause.montrer = False

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
