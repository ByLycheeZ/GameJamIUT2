import pygame

from gestionnaires.Evenement import Evenement
from interfaces.Ecran import Ecran

from interfaces.elements.Bouton import Bouton


class BoutonRetourJeu(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def evenement(self, evenement):
        if self._menu.montrer and (self._coord[0] <= pygame.mouse.get_pos()[0] <= self._coord[0] + 423) \
                and (self._coord[1] <= pygame.mouse.get_pos()[1] <= self._coord[1] + 76):
            self._menu.montrer = False

    def affichage(self, ecran):
        if self._image != "":
            image = pygame.image.load(f'res/img/interfaces/pause/{self._image}.png')
            ecran.blit(image, self._coord)