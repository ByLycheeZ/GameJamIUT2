from blocs.Bloc import Bloc


class BlocCollision(Bloc):

    def __init__(self, json, x, y, taille=1):
        super(BlocCollision, self).__init__(json, x, y, taille)

    def collisions(self, joueur, delta):
        this_rect = self._dessin.get_rect()
        this_rect.x, this_rect.y = self._x, self._y
        j_rect = joueur.get_rect_collision()
        return this_rect if this_rect.colliderect(j_rect) else None
