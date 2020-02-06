import pygame


class Bouton:
    def __init__(self, coord, image, menu):
        self._coord = coord
        self._menu = menu
        self._image = image

    def affichage(self, ecran):
        if self._image != "":
            image = pygame.image.load(f'res/img/interfaces/accueil/{self._image}.png')
            ecran.blit(image, self._coord)
