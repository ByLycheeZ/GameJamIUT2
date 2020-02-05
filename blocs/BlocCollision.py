import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from blocs.Bloc import Bloc


class BlocCollision(Bloc):

    def __init__(self, json, x, y):
        Bloc.__init(json, x, y)


    def get_Collisions(self, rect):
        this_rect = self.dessin.get_rect()
        collision = [0, 0]
        if self.dessin.get_rect().colliderect(rect):
            if (this_rect.left < rect.left and this_rect.right > rect.right) or (this_rect.left > rect.left and this_rect.right > rect.right):
                collision[0] = -1
            if (this_rect.top < rect.top and this_rect.bottom > rect.bottom) or (this_rect.top > rect.top and this_rect.bottom < rect.bottom) :
                collision[1] = -1
        return collision

