import pygame
from utils.Constantes import TAILLE_PERSO
from entites.Joueur import Joueur
from entites.Tornade import Tornade


class JoueurTornade(Joueur):
    RECHARGEMENT = 10  # En seconde

    def __init__(self, touches, couleur):
        super().__init__(touches, couleur)
        self.__dernier_lancement = pygame.time.get_ticks() * 1000

    def evenement(self, evenement):
        # if self.__vies <= 0:
        #     return
        #if (self.__dernier_lancement + JoueurTornade.RECHARGEMENT) > (pygame.time.get_ticks() * 1000):
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == self._touches.get('competence'):
                self.__competence()

        super(JoueurTornade, self).evenement(evenement)

    def maj(self, delta):
        super(JoueurTornade, self).maj(delta)

    def __competence(self):
        rect = self.get_rect()
        Tornade([rect.x+10, rect.y+10], [1, 0], self._couleur)
        self.__dernier_lancement = pygame.time.get_ticks() * 1000