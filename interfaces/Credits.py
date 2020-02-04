import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Maj import Maj


class Credits:
    def __init__(self, menu):
        self.montrer = False
        self.textes = []
        self.coord = (400, 810)
        self.menu = menu
        Affichage().enregistrer(self)
        Maj().enregistrer(self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.fill((45, 52, 54))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 40)
            self.textes.append("Léo Le Corre")
            for credit in self.textes:
                texte = font.render(credit, False, (255, 255, 255))
                ecran.blit(texte, (self.coord[0], self.coord[1]))

    def maj(self, delta):
        self.coord = (400, self.coord[1] - 50 * delta)
        if self.coord[1] <= -300:
            self.montrer = False
            self.menu.montrer = True
            self.coord = (400, 810)
