from os import listdir
from os.path import isfile, join
from random import randrange

from blocs.Chemin import Chemin
from gestionnaires.Maj import Maj
from interfaces.Ecran import Ecran
from utils.Constantes import CHEMIN_MAP
from gestionnaires.Affichage import *
from utils.Constantes import LARGEUR


class Carte:
    NEG_X_SUPPRESSION = LARGEUR

    class __Elem:
        def __init__(self, chemin, x1, x2):
            self.chemin = chemin
            self.depart = x1
            self.fin = x2

    def __init__(self):
        fichiers = [f.split('.')[0] for f in listdir(CHEMIN_MAP) if isfile(join(CHEMIN_MAP, f))]

        self.__chemins = []
        for nom_chemin in fichiers:
            self.__chemins.append(Chemin(nom_chemin))

        self.__max_x = 0
        self.__carte = []
        self.generer_carte()

        Affichage().enregistrer(self)
        Maj().enregistrer(self)

    def generer_carte(self):
        while self.__max_x < Ecran.x + 2 * LARGEUR:
            index_chemin = randrange(0, len(self.__chemins))
            chemin = self.__chemins[index_chemin]
            x1 = self.__max_x
            x2 = x1 + chemin.get_x_max()
            self.__max_x = x2
            self.__carte.append(Carte.__Elem(chemin, x1, x2))

    def maj(self, delta):
        if Ecran.x - self.__carte[0].depart > self.NEG_X_SUPPRESSION:
            self.__carte.pop(0)
            self.generer_carte()

    def affichage(self, ecran):
        for c in self.__carte:
            c.chemin.affichage(ecran, c.depart, 0)

    def fin(self):
        Affichage().supprimer(self)
        Maj().supprimer(self)
