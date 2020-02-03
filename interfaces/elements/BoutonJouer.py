import pygame

from interfaces.elements.Bouton import Bouton


class BoutonJouer(Bouton):
    def __init__(self, label, coord):
        super().__init__(label, coord)

    def afficher(self, ecran):
        image = pygame.image.load("res/bouton-jouer.png")
        ecran.blit(image, self.coord)
