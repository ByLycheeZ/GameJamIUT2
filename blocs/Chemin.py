import json

from blocs.Plateforme import Plateforme
from utils.Constantes import CHEMIN_MAP


class Chemin:
    def __init__(self, nom):
        fichier_json = open(f'{CHEMIN_MAP}/{nom}.json')
        self.__donnees = json.load(fichier_json)

        self.__plateformes = []
        self.__x_max = 0
        for plateforme in self.__donnees['disposition']:
            elem = Plateforme(self.__donnees['plateformes'][plateforme['plateforme']],
                              plateforme['x'], plateforme['y'], plateforme['taille'])

            self.__plateformes.append(elem)
            self.__x_max = max(self.__x_max, elem.get_x_max())

    def affichage(self, ecran, x, y):
        for plateforme in self.__plateformes:
            plateforme.affichage(ecran, x, y)

    def get_x_max(self):
        return self.__x_max

    def collisions(self, joueur, delta):
        collision = None
        for plateforme in self.__plateformes:
            collision = plateforme.collisions(joueur, delta)
            if collision:
                break
        return collision
