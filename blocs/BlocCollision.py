import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from blocs.Bloc import Bloc


class BlocCollision(Bloc):

    def __init__(self, json, x, y, taille=1):
        super(BlocCollision, self).__init__(json, x, y, taille)

    def get_collisions(self, rect):
        this_rect = self.__dessin.get_rect()
        collision = [0, 0]
        if self.__dessin.get_rect().colliderect(rect):
            if (this_rect.left < rect.left and this_rect.right > rect.right) or (this_rect.left > rect.left and this_rect.right > rect.right):
                collision[0] = -1
            if (this_rect.top < rect.top and this_rect.bottom > rect.bottom) or (this_rect.top > rect.top and this_rect.bottom < rect.bottom) :
                collision[1] = -1
        return collision

