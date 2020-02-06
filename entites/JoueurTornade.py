import pygame
from utils.Constantes import TAILLE_PERSO
from entites.Joueur import Joueur
from entites.Tornade import Tornade


class JoueurTornade(Joueur):
    RECHARGEMENT = 1  # En seconde

    def __init__(self, touches, couleur):
        super().__init__(touches, couleur)
        self.__cd = 0  # pour la gestions du temps

    def evenement(self, evenement):
        if self.__cd <= 0 and self._subit_tornade <= 0:
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == self._touches.get('competence'):
                    self.__competence()
                    self.__cd = self.RECHARGEMENT

        super(JoueurTornade, self).evenement(evenement)

    def maj(self, delta):
        super(JoueurTornade, self).maj(delta)
        self.__cd -= delta

    def __competence(self):
        rect = self.get_rect()
        deplacement_x = self.get_deplacement()[0]

        position_y = rect.y + (TAILLE_PERSO[1] - Tornade.TAILLE_IMAGE[1]) / 2

        if deplacement_x < 0:
            deplacement_x = -1
            position_x = rect.x - Tornade.TAILLE_IMAGE[0] + 20
        else:
            deplacement_x = 1
            position_x = rect.x + TAILLE_PERSO[0] - 20

        Tornade([position_x, position_y], [deplacement_x, 0], self._couleur)
