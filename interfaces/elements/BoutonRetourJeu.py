import pygame

from gestionnaires.Evenement import Evenement
from gestionnaires.Maj import Maj
from gestionnaires.Sons import Sons
from interfaces.Ecran import Ecran

from interfaces.elements.Bouton import Bouton


class BoutonRetourJeu(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)

    def evenement(self):
        if self._menu.montrer and (self._coord[0] <= pygame.mouse.get_pos()[0] <= self._coord[0] + 423) \
                and (self._coord[1] <= pygame.mouse.get_pos()[1] <= self._coord[1] + 76):
            Sons().jouer_son('clique', 'ogg')
            self._menu.montrer = False
            Evenement().reprendre()
            Maj().reprendre()

    def affichage(self, ecran):
        if self._image != "":
            image = pygame.image.load(f'res/img/interfaces/pause/{self._image}.png')
            ecran.blit(image, self._coord)
            
