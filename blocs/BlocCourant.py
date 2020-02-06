from blocs.BlocCollision import BlocCollision


class BlocCourant(BlocCollision):
    VITESSE = 200

    def __init__(self, json, x, y, direction):
        super(BlocCourant, self).__init__(json, x, y)
        self.direction = direction

    def collisions(self, joueur, delta):
        if self._dessin.get_rect().colliderect(joueur.get_rect()):
            joueur.get_rect().move(self.VITESSE * self.direction[0] * delta,
                                   self.VITESSE * self.direction[1] * delta)

        return None
