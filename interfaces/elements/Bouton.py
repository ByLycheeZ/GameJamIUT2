import pygame


class Bouton:
    def __init__(self, coord, image, menu):
        self._coord = coord
        self._menu = menu
        self.__image = image

    def affichage(self, ecran):
        image = pygame.image.load(f'res/img/{self.__image}.png')
        ecran.blit(image, self._coord)
