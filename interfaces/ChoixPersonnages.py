import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement


class ChoixPersonnages:
    dino_rouge = pygame.image.load("res/img/dino-rouge.png")
    dino_bleu = pygame.image.load("res/img/dino-bleu.png")
    dino_vert = pygame.image.load("res/img/dino-vert.png")
    dino_jaune = pygame.image.load("res/img/dino-jaune.png")
    dinos = [dino_rouge, dino_bleu, dino_vert, dino_jaune]
    background = pygame.image.load("res/img/accueil-background.png")

    def __init__(self):
        self.montrer = False
        self.__selection = "rouge"
        self.__coord = (100, 100)
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)

    def affichage(self, ecran):
        ecran.blit(self.background, (-490, 0))
        for dino in self.dinos:
            pass

    def evenement(self, evenement):
        pass
