import pygame
import sys
import pygame.time as time
from gestionnaires.Evenement import *
from gestionnaires.Maj import *
from gestionnaires.Affichage import *
from interfaces.MenuPrincipal import MenuPrincipal

from utils.Constantes import *

pygame.init()

ecran = pygame.display.set_mode(TAILLE)
pygame.display.set_caption("Dino Tempest")
icon = pygame.image.load("res/img/icon2.png")
pygame.display.set_icon(icon)

menu = MenuPrincipal()

clock = time.Clock()
gestionnaire_evenements = Evenement()
maj = Maj()
affichage = Affichage()


while 1:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()
        else:
            gestionnaire_evenements.maj(evenement.type, evenement)

    delta = clock.tick(MAX_IPS) / 1000
    maj.maj(delta)

    menu.affichage(ecran)
    affichage.maj(ecran)
    pygame.display.flip()
