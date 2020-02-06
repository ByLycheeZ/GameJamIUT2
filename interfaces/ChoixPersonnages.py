import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement
from gestionnaires.Images import Images

from interfaces.elements.BoutonCommencer import BoutonCommencer
from utils.Constantes import LARGEUR, HAUTEUR


class ChoixPersonnages:
    DECALAGE = 430
    COULEURS = {
        "rouge": (214, 48, 49),
        "bleu": (48, 51, 107),
        "vert": (106, 176, 76),
        "jaune": (249, 202, 36),
        "": (0, 0, 0)
    }

    class __Dino:
        def __init__(self, nom, coord=(0, 0), selectionne=False):
            self.surface = Images().charger_image(f'res/img/interfaces/selection/choix-dino-{nom}.png').convert_alpha()
            self.surface_transparent = self.surface.copy()
            self.surface_transparent.fill((255, 255, 255, 70), None, pygame.BLEND_RGBA_MULT)
            self.selectionne = selectionne
            self.coord = coord
            self.nom = nom

    class __Coeur:
        def __init__(self, i, coord=(0, 0), selectionne=False):
            self.surface = Images().charger_image('res/img/hud/coeur-rouge.bmp').convert_alpha()
            self.surface_transparent = self.surface.copy()
            self.surface_transparent.fill((255, 255, 255, 70), None, pygame.BLEND_RGBA_MULT)
            self.selectionne = selectionne
            self.coord = coord
            self.index = i + 1

        def collision(self, point):
            rect = self.surface.get_rect()
            rect.x, rect.y = self.coord

            return rect.collidepoint(point)

    def __init__(self, menu):
        self.montrer = False
        self.__menu = menu
        self.__bouton_commencer = BoutonCommencer((750, 380), "bouton-commencer", self)
        self.__selection_joueur_1 = ""
        self.__selection_joueur_2 = ""
        self.__dino_rouge = self.__Dino("rouge", (0, 70))
        self.__dino_bleu = self.__Dino("bleu", (250, 70))
        self.__dino_vert = self.__Dino("vert", (500, 70))
        self.__dino_jaune = self.__Dino("jaune", (750, 70))
        self.__dinos = {
            "rouge": self.__dino_rouge,
            "bleu": self.__dino_bleu,
            "vert": self.__dino_vert,
            "jaune": self.__dino_jaune
        }

        font = pygame.font.Font('res/fonts/Comfortaa-Bold.ttf', 30)
        self.__difficulte = font.render('Niveau de difficulté : ', True, (255, 255, 255))

        self.__coeurs = []
        for i in range(3):
            self.__coeurs.append(self.__Coeur(i, (LARGEUR / 2 - 50 + i * 40, HAUTEUR / 2 - 30), True))
        for i in range(3, 5):
            self.__coeurs.append(self.__Coeur(i, (LARGEUR / 2 - 50 + i * 40, HAUTEUR / 2 - 30)))

        self.__background = Images().charger_image("res/img/interfaces/accueil/accueil-background.png")
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.__background, (0, 0))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 60)
            # Joueur 1
            ecran.blit(font.render('Joueur 1', True, self.COULEURS[self.__selection_joueur_1]), (35, 10))
            pygame.draw.rect(ecran, self.COULEURS[self.__selection_joueur_1], ((40, 90), (940, 210)), 3)

            # Joueur 2
            ecran.blit(font.render('Joueur 2', True, self.COULEURS[self.__selection_joueur_2]), (35, 435))
            pygame.draw.rect(ecran, self.COULEURS[self.__selection_joueur_2], ((40, 515), (940, 210)), 3)

            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            ecran.blit(font.render('ESC pour retourner au menu principal', True, (48, 51, 107)), (600, 3))
            self.__bouton_commencer.affichage(ecran)
            n_ieme = 0
            for dino in self.__dinos.values():
                if self.__selection_joueur_1 == dino.nom:
                    image = dino.surface.subsurface(pygame.Rect(0, 0, 240, 240))
                else:
                    image = dino.surface_transparent.subsurface(pygame.Rect(0, 0, 240, 240))
                ecran.blit(image, (250 * n_ieme, 70))
                if self.__selection_joueur_2 == dino.nom:
                    image = dino.surface.subsurface(pygame.Rect(0, 0, 240, 240))
                else:
                    image = dino.surface_transparent.subsurface(pygame.Rect(0, 0, 240, 240))
                ecran.blit(image, (250 * n_ieme, 70 + self.DECALAGE))
                n_ieme += 1
            ecran.blit_absolu(self.__difficulte, (80, HAUTEUR / 2 - 30))
            for coeur in self.__coeurs:
                if coeur.selectionne:
                    ecran.blit_absolu(coeur.surface, coeur.coord)
                else:
                    ecran.blit_absolu(coeur.surface_transparent, coeur.coord)

    def evenement(self, evenement):
        if self.montrer:
            if evenement.type == pygame.MOUSEBUTTONUP:
                for couleur, dino in self.__dinos.items():
                    if (dino.coord[0] + 30 <= pygame.mouse.get_pos()[0] <= dino.coord[0] + 190) \
                            and (dino.coord[1] + 40 <= pygame.mouse.get_pos()[1] <= dino.coord[1] + 210):
                        if not dino.selectionne:
                            if self.__selection_joueur_1 != "":
                                self.__dinos.get(self.__selection_joueur_1).selectionne = False
                            self.__selection_joueur_1 = couleur
                            dino.selectionne = True
                    elif (dino.coord[0] + 30 <= pygame.mouse.get_pos()[0] <= dino.coord[0] + 190) \
                            and (dino.coord[1] + 40 + self.DECALAGE <= pygame.mouse.get_pos()[1] <= dino.coord[1] + 200 + self.DECALAGE):
                        if not dino.selectionne:
                            if self.__selection_joueur_2 != "":
                                self.__dinos.get(self.__selection_joueur_2).selectionne = False
                            self.__selection_joueur_2 = couleur
                            dino.selectionne = True
                for coeur in self.__coeurs:
                    if coeur.collision(pygame.mouse.get_pos()):
                        for i in range(0, coeur.index):
                            self.__coeurs[i].selectionne = True
                        for i in range(coeur.index, len(self.__coeurs)):
                            self.__coeurs[i].selectionne = False
                if not self.__selection_joueur_1 == "" and not self.__selection_joueur_2 == "":
                    self.__bouton_commencer.transparent = False
            elif evenement.type == pygame.KEYUP:
                if evenement.key == pygame.K_ESCAPE and self.montrer:
                    for dino in self.__dinos.values():
                        dino.selectionne = False
                        self.__selection_joueur_1 = ""
                        self.__selection_joueur_2 = ""
                    self.__bouton_commencer.transparent = True
                    self.montrer = False
                    self.__menu.montrer = True

    def get_selection_j1(self):
        return self.__selection_joueur_1

    def get_selection_j2(self):
        return self.__selection_joueur_2

    def get_nb_coeurs(self):
        i = 0
        while i < len(self.__coeurs) and self.__coeurs[i].selectionne:
            i += 1

        return i
