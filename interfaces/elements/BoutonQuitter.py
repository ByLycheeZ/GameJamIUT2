import pygame

from gestionnaires.Evenement import Evenement
from interfaces.elements.Bouton import Bouton


class BoutonQuitter(Bouton):
    def __init__(self, label, coord):
        super().__init__(label, coord)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def afficher(self, ecran):
        image = pygame.image.load("res/bouton-quitter.png")
        ecran.blit(image, self.coord)

    def evenement(self, evenement):
        if (self.coord[0] <= pygame.mouse.get_pos()[0] <= self.coord[0] + 300) \
                and (self.coord[1] <= pygame.mouse.get_pos()[1] <= self.coord[1] + 76):
            quit()
