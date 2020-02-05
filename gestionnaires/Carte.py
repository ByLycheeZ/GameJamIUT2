from os import listdir
from os.path import isfile, join

from blocs.Chemin import Chemin
from utils.Constantes import CHEMIN_MAP
from gestionnaires.Affichage import *


class Carte:
    def __init__(self):
        fichiers = [f.split('.')[0] for f in listdir(CHEMIN_MAP) if isfile(join(CHEMIN_MAP, f))]

        self.chemins = []
        for nom_chemin in fichiers:
            self.chemins.append(Chemin(nom_chemin))

        Affichage().enregistrer(self)

    def affichage(self, ecran):
        for chemin in self.chemins:
            chemin.affichage(ecran, 0, 0)

    def fin(self):
        Affichage().supprimer(self)