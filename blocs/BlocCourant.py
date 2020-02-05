from blocs.BlocCollision import BlocCollision


class BlocCourant(BlocCollision):
    VITESSE = 200
    def __init__(self, json, x, y, direction):
        BlocCollision.__init(json, x, y)
        self.direction = direction

    def get_collisions(self, joueur, delta):
        if self.dessin.get_rect().colliderect(joueur.get_rect()):
            joueur.get_rect().move(self.VITESSE * self.direction[0] * delta,
                                   self.VITESSE * self.direction[1] * delta)

        return [0, 0]
