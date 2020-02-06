from blocs.BlocCollision import BlocCollision


class BlocCourant(BlocCollision):

    def __init__(self, json, x, y, taille, direction, vitesse):
        super(BlocCourant, self).__init__(json, x, y, taille)
        self.__direction = direction
        self.__vitesse = vitesse

    def collisions(self, joueur, delta):
        this_rect = self._dessin.get_rect()
        this_rect.x, this_rect.y = self._x, self._y

        if this_rect.colliderect(joueur.get_rect_collision()):
            joueur.ajouter_boost(*[self.__vitesse * delta * x for x in self.__direction])

        return None
