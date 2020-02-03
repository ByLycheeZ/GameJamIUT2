import pygame

from interfaces.elements.Bouton import Bouton


class BoutonQuitter(Bouton):
    def __init__(self, label, coord):
        super().__init__(label, coord)

    def afficher(self, ecran):
        image = pygame.image.load("res/bouton-quitter.png")
        ecran.blit(image, self.coord)
