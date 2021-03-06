import pygame

from gestionnaires.Evenement import Evenement
from gestionnaires.Images import Images
from gestionnaires.Jeu import Jeu
from gestionnaires.Sons import Sons

from interfaces.elements.Bouton import Bouton


class BoutonCommencer(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)
        self.transparent = True
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def evenement(self, evenement):
        if self._menu.montrer:
            if not self.transparent:
                if (self._coord[0] <= pygame.mouse.get_pos()[0] <= self._coord[0] + 241) \
                        and (self._coord[1] <= pygame.mouse.get_pos()[1] <= self._coord[1] + 66):
                    self._menu.montrer = False
                    Sons().jouer_son('clique', 'ogg')
                    Jeu([self._menu.get_selection_j1(), self._menu.get_selection_j2()], self._menu.get_nb_coeurs())

    def affichage(self, ecran):
        nom = self._image
        if self.transparent:
            image = Images().charger_image(f'res/img/interfaces/selection/{nom}-desactive.png')
        else:
            image = Images().charger_image(f'res/img/interfaces/selection/{nom}.png')
        ecran.blit(image, self._coord)
