import pygame

from gestionnaires.Evenement import Evenement
from gestionnaires.Sons import Sons

from interfaces.elements.Bouton import Bouton


class BoutonSources(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def evenement(self, evenement):
        if self._menu.equipe:
            if (self._coord[0] <= pygame.mouse.get_pos()[0] <= self._coord[0] + 135) \
                    and (self._coord[1] <= pygame.mouse.get_pos()[1] <= self._coord[1] + 40):
                Sons().jouer_son('clique', 'ogg')
                self.afficher_sources()

    def afficher_sources(self):
        self._menu.equipe = False
        self._menu.sources = True
