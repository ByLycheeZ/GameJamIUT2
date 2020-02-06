import os
import pygame

from gestionnaires.Affichage import Affichage
from utils.Constantes import LARGEUR
from datetime import datetime, timedelta


class HudMeilleurTemps:
    CHEMIN_FICHIER = 'highscore.txt'

    def __init__(self):
        self.__temps = None

        if os.path.isfile(self.CHEMIN_FICHIER):
            f = open(self.CHEMIN_FICHIER, 'r')
            self.__temps = f.readline()
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 24)
            self.__texte = font.render(f'Plus longue survie : {self.__temps[:-3]}', True, (255, 255, 225))
            Affichage().enregistrer(self, 5)

        self.__debut = pygame.time.get_ticks()

    def fin(self):
        temps = timedelta(milliseconds=pygame.time.get_ticks() - self.__debut)
        delta = timedelta(milliseconds=0)
        if self.__temps:
            t = datetime.strptime(self.__temps, "%H:%M:%S.%f")
            delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        if temps > delta:
            f = open(self.CHEMIN_FICHIER, 'w')
            f.write(str(temps))
        Affichage().supprimer(self)

    def affichage(self, ecran):
        ecran.blit_absolu(self.__texte, (LARGEUR / 2 - self.__texte.get_width() / 2, 10))
