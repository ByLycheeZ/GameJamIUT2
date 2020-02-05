from blocs.BlocCollision import BlocCollision


class BlocCourant(BlocCollision):

    def __init__(self, json, x, y, direction):
        BlocCollision.__init(json, x, y)
        self.direction = direction

    def get_collisions(self, rect):
        if self.dessin.get_rect().colliderect(rect):
            return self.direction
        else:
            return [0, 0]
