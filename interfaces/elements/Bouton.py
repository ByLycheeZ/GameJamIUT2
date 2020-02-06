import pygame

from gestionnaires.Images import Images


class Bouton:
    def __init__(self, coord, image, menu):
        self._coord = coord
        self._menu = menu
        self._image = image

    def affichage(self, ecran):
        if self._image != "":
            image = Images().charger_image(f'res/img/interfaces/accueil/{self._image}.png')
            ecran.blit(image, self._coord)
