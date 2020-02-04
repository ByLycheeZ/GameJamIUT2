import pygame
import sys
import pygame.time as time
from gestionnaires.Evenement import *
from gestionnaires.Maj import *
from entites.Joueur import Joueur
from decorations.Parallax import Parallax
from interfaces.Ecran import Ecran

from utils.Constantes import *

pygame.init()

ecran = pygame.display.set_mode(TAILLE)

clock = time.Clock()
gestionnaire_evenements = Evenement()
maj = Maj()
affichage = Ecran(ecran)

parallax = Parallax()
joueur = Joueur({'aller_gauche': pygame.K_q, 'aller_droite': pygame.K_d, 'sauter': pygame.K_z})
joueur2 = Joueur({'aller_gauche': pygame.K_LEFT, 'aller_droite': pygame.K_RIGHT, 'sauter': pygame.K_UP})
while 1:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()
        else:
            gestionnaire_evenements.maj(evenement.type, evenement)

    delta = clock.tick(MAX_IPS) / 1000
    maj.maj(delta)

    ecran.fill(FOND)
    affichage.affichage(ecran)
    pygame.display.flip()
