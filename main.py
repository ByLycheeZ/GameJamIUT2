import pygame
import sys
import pygame.time as time
from gestionnaires.Evenement import *
from gestionnaires.Maj import *
from gestionnaires.Affichage import *
from exemple.Balle import Balle

from utils.Constantes import *

pygame.init()

ecran = pygame.display.set_mode(TAILLE)

clock = time.Clock()
gestionnaire_evenements = Evenement()
maj = Maj()
affichage = Affichage()

balle = Balle()


while 1:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()
        else:
            gestionnaire_evenements.maj(evenement.type, evenement)

    delta = clock.tick(MAX_IPS) / 1000
    maj.maj(delta)

    ecran.fill(FOND)
    affichage.maj(ecran)
    pygame.display.flip()
