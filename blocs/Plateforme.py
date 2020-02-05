import importlib
from blocs.Bloc import Bloc
from blocs.BlocCollision import BlocCollision
from gestionnaires.Affichage import Affichage


class Plateforme:
    class __Elem:
        def __init__(self, nom, x, y, taille, collision, nom_module, nom_classe, attrs):
            if nom_module and nom_classe and attrs:
                module = importlib.import_module(nom_module)
                classe = getattr(module, nom_classe)
                self.bloc = classe(nom, 0, 0, taille, *attrs)
            else:
                if collision:
                    self.bloc = BlocCollision(nom, 0, 0, taille)
                else:
                    self.bloc = Bloc(nom, 0, 0, taille)
            Affichage().supprimer(self.bloc)
            self.x = x
            self.y = y

    def __init__(self, donnees, x, y, taille):
        self.__blocs = []
        self.__x_max = 0
        for bloc in donnees:
            module, classe, attr = None, None, []
            if all(cle in bloc for cle in ['module', 'classe', 'attributs']):
                module = bloc['module']
                classe = bloc['classe']
                attr = bloc['attributs']

            elem = Plateforme.__Elem(bloc['source'], bloc['x'] + x, bloc['y'] + y, taille, bloc['collision'],
                                     module, classe, attr)
            self.__blocs.append(elem)
            self.__x_max = max([self.__x_max, elem.x + elem.bloc.get_largeur()])

    def affichage(self, ecran, x, y):
        for b in self.__blocs:
            b.bloc.set_x(x + b.x)
            b.bloc.set_y(y + b.y)
            b.bloc.affichage(ecran)

    def get_x_max(self):
        return self.__x_max

    def collisions(self, joueur, delta):
        collision = None
        for e in self.__blocs:
            collision = e.bloc.collisions(joueur, delta)
            if collision:
                break

        return collision
