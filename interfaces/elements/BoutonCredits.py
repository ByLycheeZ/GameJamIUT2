import pygame

from gestionnaires.Evenement import Evenement

from interfaces.elements.Bouton import Bouton


class BoutonCredits(Bouton):
    def __init__(self, coord, image, menu):
        super().__init__(coord, image, menu)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def evenement(self, evenement):
        if (self.coord[0] <= pygame.mouse.get_pos()[0] <= self.coord[0] + 100) \
                and (self.coord[1] <= pygame.mouse.get_pos()[1] <= self.coord[1] + 30):
            self.afficher_credits()

    def afficher_credits(self):
        self.menu.montrer = False
        self.menu.credits.montrer = True
