import pygame

from gestionnaires.Affichage import Affichage


class Bouton:
    def __init__(self, coord, image, menu):
        self.coord = coord
        self.image = image
        self.menu = menu
        Affichage().enregistrer(self)

    def affichage(self, ecran):
        image = pygame.image.load("res/img/" + self.image + ".png")
        ecran.blit(image, self.coord)
