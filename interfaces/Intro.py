import pygame, math, time

from gestionnaires.Affichage import Affichage
from gestionnaires.Maj import Maj
from gestionnaires.Sons import Sons
from interfaces.MenuPrincipal import MenuPrincipal
from utils.Constantes import *


class Intro:

    def __init__(self):
        self.montrer = True
        self.__couleur = (180, 180, 180)
        self.__timeur = 0
        self.__temps = 0
        self.__compteur = 0
        self.__image = pygame.image.load("res/img/interfaces/intro/carryboo.png").convert_alpha()
        self.__image.fill((255, 255, 255, 15), None, pygame.BLEND_RGBA_MULT)
        Affichage().enregistrer(self)
        Maj().enregistrer(self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.fill(self.__couleur)
            for i in range(min(30, self.__compteur)):
                ecran.blit(self.__image, (LARGEUR/2 - 126, HAUTEUR/2 - 230))
            if self.__timeur == 300:
                Sons().jouer_son('intro', 'ogg')
            if self.__timeur == 1300:
                self.montrer = False
                self.__timeur = 0
                MenuPrincipal()

    def maj(self, delta):
        if self.montrer:
            self.__temps += delta
            if self.__temps >= 1/(17*2):
                self.__temps -= 1/(17*2)
                self.__compteur += 1
                self.__timeur += 10

