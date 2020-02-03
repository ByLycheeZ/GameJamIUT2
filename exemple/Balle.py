import pygame
from gestionnaires.Evenement import *
from gestionnaires.Maj import *
from gestionnaires.Affichage import *


class Balle:
    def __init__(self):
        self.vitesse = 300
        self.direction = [0, 0]
        self.balle = pygame.image.load("res/intro_ball.gif")
        self.balle_rect = self.balle.get_rect()

        evenement = Evenement()
        evenement.enregistrer(pygame.KEYDOWN, self)
        evenement.enregistrer(pygame.KEYUP, self)

        Maj().enregistrer(self)
        Affichage().enregistrer(self)

    def evenement(self, evenement):
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_z:
                self.direction[1] -= 1
            elif evenement.key == pygame.K_s:
                self.direction[1] += 1
            elif evenement.key == pygame.K_q:
                self.direction[0] -= 1
            elif evenement.key == pygame.K_d:
                self.direction[0] += 1
        else:
            if evenement.key == pygame.K_z:
                self.direction[1] += 1
            elif evenement.key == pygame.K_s:
                self.direction[1] -= 1
            elif evenement.key == pygame.K_q:
                self.direction[0] += 1
            elif evenement.key == pygame.K_d:
                self.direction[0] -= 1

    def maj(self, delta):
        self.balle_rect = self.balle_rect.move(int(self.vitesse * self.direction[0] * delta),
                                               int(self.vitesse * self.direction[1] * delta))

    def affichage(self, ecran):
        ecran.blit(self.balle, self.balle_rect)