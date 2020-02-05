import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement

from interfaces.elements.BoutonEquipe import BoutonEquipe
from interfaces.elements.BoutonSources import BoutonSources

from utils import Constantes


class Credits:
    TURQUOISE = (26, 188, 156)
    BLANC = (255, 255, 255)
    BLEU = (41, 128, 185)

    def __init__(self, menu):
        self.montrer = False
        self.equipe = True
        self.sources = False
        self.__menu = menu
        self.__bouton_sources = BoutonSources((880, 730), "", self)
        self.__bouton_equipe = BoutonEquipe((10, 730), "", self)
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            background = pygame.image.load("res/img/interfaces/accueil/accueil-background.png")
            ecran.blit(background, (-490, 0))
            if self.equipe and not self.sources:
                image = pygame.image.load("res/img/interfaces/credits/credits.png")

                # Titre
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 80)
                texte = font.render("Equipe", True, self.TURQUOISE)
                ecran.blit(texte, (Constantes.LARGEUR/2 - texte.get_width()/2, 30))

                # Noms
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
                ecran.blit(font.render("Baptiste LEDOYEN", True, self.BLEU), (30, 170))
                ecran.blit(font.render("Thibault GROOT", True, self.BLEU), (30, 350))
                ecran.blit(font.render("Théo PONCHON", True, self.BLEU), (650, 170))
                ecran.blit(font.render("Thomas VINCENT", True, self.BLEU), (650, 350))
                ecran.blit(font.render("Léo LE CORRE", True, self.BLEU), (Constantes.LARGEUR/2 - texte.get_width()/2, 530))

                # Rôles
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 26)
                # Baptiste
                ecran.blit(font.render("Chef de projet", True, self.BLANC), (90, 220))
                ecran.blit(font.render("Développeur", True, self.BLANC), (90, 260))
                # Théo
                ecran.blit(font.render("Développeur UI", True, self.BLANC), (700, 220))
                ecran.blit(font.render("Designer", True, self.BLANC), (700, 260))
                # Thibault
                ecran.blit(font.render("Développeur", True, self.BLANC), (90, 260))
                # Thomas
                ecran.blit(font.render("Développeur", True, self.BLANC), (90, 260))

                # Bouton Sources
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 30)
                texte = font.render("Sources", True, self.TURQUOISE)
                ecran.blit(texte, (880, 720))

            elif self.sources and not self.equipe:
                image = pygame.image.load("res/img/interfaces/credits/images-sons.png")

                # Titre
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 80)
                texte = font.render("Sources", True, self.TURQUOISE)
                ecran.blit(texte, (Constantes.LARGEUR/2 - texte.get_width()/2, 30))

                # Bouton Equipe
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 30)
                texte = font.render("Equipe", True, self.TURQUOISE)
                ecran.blit(texte, (10, 720))

            # Instruction ESC
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            texte = font.render("ESC pour retourner au menu principal", True, self.BLANC)
            ecran.blit(texte, (Constantes.LARGEUR/2 - texte.get_width()/2, 740))

    def evenement(self, evenement):
        if self.montrer and evenement.key == pygame.K_ESCAPE:
            self.montrer = False
            self.equipe = True
            self.sources = False
            self.__menu.montrer = True
