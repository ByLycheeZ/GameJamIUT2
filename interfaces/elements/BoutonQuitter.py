import pygame

from gestionnaires.Evenement import Evenement

from interfaces.elements.Bouton import Bouton


class BoutonQuitter(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def evenement(self, evenement):
        if (self._coord[0] <= pygame.mouse.get_pos()[0] <= self._coord[0] + 300) \
                and (self._coord[1] <= pygame.mouse.get_pos()[1] <= self._coord[1] + 76):
            quit()
