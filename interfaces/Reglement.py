import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement

from utils import Constantes


class Reglement:
    TITRE = (26, 188, 156)  # Turquoise
    SOUS_TITRE = (41, 128, 185)  # Bleu
    DESCRIPTION = (255, 255, 255)  # Blanc

    def __init__(self, menu):
        self.montrer = False
        self.__menu = menu
        self.__background = pygame.image.load("res/img/interfaces/accueil/accueil-background.png")
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.__background, (-490, 0))

            # Titre
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 60)
            texte = font.render("Règles", True, self.TITRE)
            ecran.blit(texte, (Constantes.LARGEUR / 2 - texte.get_width() / 2, 20))

            # Objectif
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
            ecran.blit(font.render("Objectif", True, self.SOUS_TITRE), (50, 110))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            ecran.blit(font.render("Soyez le dernier en vie en utilisant les", True, self.DESCRIPTION), (50, 160))
            ecran.blit(font.render("courants ascendants et descendants", True, (155, 89, 182)), (455, 160))
            ecran.blit(font.render("pour changer", True, self.DESCRIPTION), (860, 160))
            ecran.blit(font.render("d'étages. Vous disposez également d'une", True, self.DESCRIPTION), (50, 187))
            ecran.blit(font.render("compétence unique", True, (230, 126, 34)), (490, 187))
            ecran.blit(font.render(", propre à chaque dinosaure.", True, self.DESCRIPTION), (705, 187))
            ecran.blit(font.render("Evitez les obstacles et courez, la caméra se déplace en fonction du joueur en première", True, self.DESCRIPTION), (50, 214))
            ecran.blit(font.render("position. Si vous sortez de l'écran (à gauche) vous perdez une vie et réapparessez au", True, self.DESCRIPTION), (50, 241))
            ecran.blit(font.render("centre de l'écran. Vous ne possédez que", True, self.DESCRIPTION), (50, 268))
            ecran.blit(font.render("5 vies", True, (231, 76, 60)), (485, 268))
            ecran.blit(font.render(".", True, self.DESCRIPTION), (550, 268))

            # Commandes
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
            ecran.blit(font.render("Commandes", True, self.SOUS_TITRE), (50, 320))


            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            texte = font.render("ESC pour retourner au menu principal", True, self.DESCRIPTION)
            ecran.blit(texte, (Constantes.LARGEUR/2 - texte.get_width()/2, 740))

    def evenement(self, evenement):
        if self.montrer and evenement.key == pygame.K_ESCAPE:
            self.montrer = False
            self.__menu.montrer = True
