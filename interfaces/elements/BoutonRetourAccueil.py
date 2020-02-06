import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement
from gestionnaires.Maj import Maj

from interfaces.elements.Bouton import Bouton


class BoutonRetourAccueil(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)

    def evenement(self):
        if self._menu.montrer and (self._coord[0] <= pygame.mouse.get_pos()[0] <= self._coord[0] + 605) \
                and (self._coord[1] <= pygame.mouse.get_pos()[1] <= self._coord[1] + 76):
            self._menu.montrer = False
            self._menu.fin()
            Evenement().reprendre()
            Maj().reprendre()

    def affichage(self, ecran):
        if self._image != "":
            image = pygame.image.load(f'res/img/interfaces/pause/{self._image}.png')
            ecran.blit(image, self._coord)

    def retour_menu_principal(self):
        aff = Affichage()
        aff.supprimer(self._menu)
        
