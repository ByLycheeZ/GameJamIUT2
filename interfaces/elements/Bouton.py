import pygame


class Bouton:
    def __init__(self, coord, image, menu):
        self.coord = coord
        self.image = image
        self.menu = menu

    def afficher(self, ecran):
        image = pygame.image.load("res/" + self.image + ".png")
        ecran.blit(image, self.coord)