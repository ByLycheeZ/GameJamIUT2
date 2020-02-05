import pygame

from gestionnaires.Evenement import Evenement

from interfaces.elements.Bouton import Bouton


class BoutonEquipe(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def evenement(self, evenement):
        if self._menu.sources:
            if (self._coord[0] <= pygame.mouse.get_pos()[0] <= self._coord[0] + 135) \
                    and (self._coord[1] <= pygame.mouse.get_pos()[1] <= self._coord[1] + 40):
                self.afficher_equipe()

    def afficher_equipe(self):
        self._menu.equipe = True
        self._menu.sources = False
