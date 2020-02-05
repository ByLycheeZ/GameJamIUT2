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
        for plateforme in self.__donnees['disposition']:
            self.__plateformes.append(Chemin.__Elem(self.__donnees['plateformes'][plateforme['plateforme']],
                                                    plateforme['x'], plateforme['y'], plateforme['taille']))

    def affichage(self, ecran, x, y):
        for p in self.__plateformes:
            p.plateforme.affichage(ecran, x, y)
