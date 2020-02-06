from blocs.BlocCollision import BlocCollision
from gestionnaires.Sons import Sons


class BlocCourant(BlocCollision):

    def __init__(self, json, x, y, taille, direction, vitesse):
        super(BlocCourant, self).__init__(json, x, y, taille)
        self.__direction = direction
        self.__vitesse = vitesse
        self.__joueurs = []

    def collisions(self, joueur, delta):
        this_rect = self.get_rect()
        this_rect.x, this_rect.y = self._x, self._y

        if this_rect.colliderect(joueur.get_rect_collision()):
            joueur.ajouter_boost(*[self.__vitesse * delta * x for x in self.__direction])
            if joueur not in self.__joueurs:
                Sons().jouer_son('vent')
                self.__joueurs.append(joueur)
        elif joueur in self.__joueurs:
            self.__joueurs.remove(joueur)

        return None
