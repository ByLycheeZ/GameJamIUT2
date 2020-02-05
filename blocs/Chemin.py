import json

from blocs.Plateforme import Plateforme
from utils.Constantes import CHEMIN_MAP


class Chemin:
    class __Elem:
        def __init__(self, donnees, x, y, taille):
            self.plateforme = Plateforme(donnees, x, y, taille)

    def __init__(self, nom):
        fichier_json = open(f'{CHEMIN_MAP}/{nom}.json')
        self.__donnees = json.load(fichier_json)

        self.__plateformes = []
        self.__x_max = 0
        for plateforme in self.__donnees['disposition']:
            elem = Chemin.__Elem(self.__donnees['plateformes'][plateforme['plateforme']],
                                 plateforme['x'], plateforme['y'], plateforme['taille'])

            self.__plateformes.append(elem)
            self.__x_max = max(self.__x_max, elem.plateforme.get_x_max())

    def affichage(self, ecran, x, y):
        for p in self.__plateformes:
            p.plateforme.affichage(ecran, x, y)

    def get_x_max(self):
        return self.__x_max
