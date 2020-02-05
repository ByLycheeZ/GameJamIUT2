from blocs.Bloc import Bloc
from gestionnaires.Affichage import Affichage


class Plateforme:
    class __Elem:
        def __init__(self, nom, x, y, taille):
            self.bloc = Bloc(nom, 0, 0, taille)
            Affichage().supprimer(self.bloc)
            self.x = x
            self.y = y

    def __init__(self, donnees, x, y, taille):
        self.__blocs = []
        for bloc in donnees:
            self.__blocs.append(Plateforme.__Elem(bloc['source'], bloc['x'] + x, bloc['y'] + y, taille))

    def affichage(self, ecran, x, y):
        for b in self.__blocs:
            b.bloc.set_x(x + b.x)
            b.bloc.set_y(y + b.y)
            b.bloc.affichage(ecran)
