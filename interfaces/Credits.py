import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement
from gestionnaires.Images import Images

from interfaces.elements.BoutonEquipe import BoutonEquipe
from interfaces.elements.BoutonSources import BoutonSources

from utils.Constantes import *


class Credits:
    TITRE = (48, 51, 107)  # Bleu marine
    NOM = (249, 202, 36)  # Jaune
    DESCRIPTION = (255, 255, 255)  # Blanc
    NOM_X = 30
    DESC_X = 350

    def __init__(self, menu):
        self.montrer = False
        self.equipe = True
        self.sources = False
        self.__menu = menu
        self.__bouton_sources = BoutonSources((880, 715), "", self)
        self.__bouton_equipe = BoutonEquipe((10, 715), "", self)
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            background = Images().charger_image("res/img/interfaces/accueil/accueil-background.png")
            ecran.blit(background, (0, 0))
            if self.equipe and not self.sources:
                # Titre
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 80)
                texte = font.render("Equipe", True, self.TITRE)
                ecran.blit(texte, (LARGEUR/2 - texte.get_width()/2, 30))

                # Noms
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
                ecran.blit(font.render("Baptiste LEDOYEN", True, self.NOM), (30, 170))
                ecran.blit(font.render("Thomas VINCENT", True, self.NOM), (30, 350))
                ecran.blit(font.render("Thibault GROOT", True, self.NOM), (670, 350))
                ecran.blit(font.render("Théo PONCHON", True, self.NOM), (670, 170))
                texte = font.render("Léo LE CORRE", True, self.NOM)
                ecran.blit(texte, (LARGEUR/2 - texte.get_width()/2, 530))

                # Rôles
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 26)
                # Baptiste
                ecran.blit(font.render("Chef de projet", True, self.DESCRIPTION), (90, 220))
                ecran.blit(font.render("Développeur", True, self.DESCRIPTION), (90, 260))
                # Thomas
                ecran.blit(font.render("Responsable technique", True, self.DESCRIPTION), (30, 400))
                ecran.blit(font.render("Développeur", True, self.DESCRIPTION), (90, 440))
                # Thibault
                ecran.blit(font.render("Développeur", True, self.DESCRIPTION), (720, 400))
                # Théo
                ecran.blit(font.render("Développeur UI", True, self.DESCRIPTION), (720, 220))
                ecran.blit(font.render("Designer", True, self.DESCRIPTION), (720, 260))
                # Léo
                texte = font.render("Game Designer", True, self.DESCRIPTION)
                ecran.blit(texte, (LARGEUR/2 - texte.get_width()/2 + 30, 580))

                # Bouton Sources
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 30)
                ecran.blit(font.render("Sources", True, self.TITRE), (880, 720))

            elif self.sources and not self.equipe:
                # Titre
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 80)
                texte = font.render("Sources", True, self.TITRE)
                ecran.blit(texte, (LARGEUR/2 - texte.get_width()/2, 30))

                # Bouton Equipe
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 30)
                ecran.blit(font.render("Equipe", True, self.TITRE), (10, 720))

                # Ressources
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
                ecran.blit(font.render("Tileset", True, self.NOM), (self.NOM_X, 150))
                ecran.blit(font.render("Parallax", True, self.NOM), (self.NOM_X, 180))
                ecran.blit(font.render("Dinosaures", True, self.NOM), (self.NOM_X, 210))
                ecran.blit(font.render("Coeur HUD", True, self.NOM), (self.NOM_X, 240))
                ecran.blit(font.render("Tornade", True, self.NOM), (self.NOM_X, 270))

                ecran.blit(font.render("Musique", True, self.NOM), (self.NOM_X, 360))
                ecran.blit(font.render("Musique alternative", True, self.NOM), (self.NOM_X, 390))
                ecran.blit(font.render("Son de vent", True, self.NOM), (self.NOM_X, 450))
                ecran.blit(font.render("Son de fin", True, self.NOM), (self.NOM_X, 480))
                ecran.blit(font.render("Son de fin alternatif", True, self.NOM), (self.NOM_X, 510))
                ecran.blit(font.render("Son de mort", True, self.NOM), (self.NOM_X, 540))
                ecran.blit(font.render("Son de mort alternatif", True, self.NOM), (self.NOM_X, 570))

                # Liens
                font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 15)
                ecran.blit(font.render("https://bigbuckbunny.itch.io/platform-assets-pack", True, self.DESCRIPTION), (self.DESC_X, 153))
                ecran.blit(font.render("https://mamanezakon.itch.io/forest-tileset", True, self.DESCRIPTION), (self.DESC_X, 183))
                ecran.blit(font.render("https://arks.itch.io/dino-characters", True, self.DESCRIPTION), (self.DESC_X, 213))
                ecran.blit(font.render("https://opengameart.org/content/pixel-hearts", True, self.DESCRIPTION), (self.DESC_X, 243))
                ecran.blit(font.render("https://opengameart.org/content/spells-and-company", True, self.DESCRIPTION), (self.DESC_X, 273))

                ecran.blit(font.render("https://www.fesliyanstudios.com/royalty-free-music/download/retro-platforming/454", True, self.DESCRIPTION), (self.DESC_X, 363))
                ecran.blit(font.render("https://freemusicarchive.org/music/sawsquarenoise/Towel_Defence_OST/", True, self.DESCRIPTION), (self.DESC_X, 393))
                ecran.blit(font.render("Towel_Defence_Ingame", True, self.DESCRIPTION), (self.DESC_X, 410))
                ecran.blit(font.render("https://lasonotheque.org/detail-0595-vent.html", True, self.DESCRIPTION), (self.DESC_X, 453))
                ecran.blit(font.render("https://opengameart.org/content/crash-collision", True, self.DESCRIPTION), (self.DESC_X, 483))
                ecran.blit(font.render("https://opengameart.org/content/15-monster-gruntpaindeath-sounds", True, self.DESCRIPTION), (self.DESC_X, 513))
                ecran.blit(font.render("http://soundbible.com/1569-I-Will-Kill-You.html", True, self.DESCRIPTION), (self.DESC_X, 543))
                ecran.blit(font.render("http://soundbible.com/1459-Psycho-Scream.html", True, self.DESCRIPTION), (self.DESC_X, 573))

            # Instruction ESC
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            texte = font.render("ESC pour retourner au menu principal", True, self.DESCRIPTION)
            ecran.blit(texte, (LARGEUR/2 - texte.get_width()/2, 740))

    def evenement(self, evenement):
        if self.montrer and evenement.key == pygame.K_ESCAPE:
            self.montrer = False
            self.equipe = True
            self.sources = False
            self.__menu.montrer = True
