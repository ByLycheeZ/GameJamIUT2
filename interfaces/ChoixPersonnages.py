import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement
from gestionnaires.Images import Images

from interfaces.elements.BoutonCommencer import BoutonCommencer


class ChoixPersonnages:
    DECALAGE = 430

    class __Dino:
        def __init__(self, nom, coord=(0, 0), selectionne=False):
            self.surface = Images().charger_image(f'res/img/interfaces/selection/choix-dino-{nom}.png').convert_alpha()
            self.surface_transparent = self.surface.copy()
            self.surface_transparent.fill((255, 255, 255, 70), None, pygame.BLEND_RGBA_MULT)
            self.selectionne = selectionne
            self.coord = coord
            self.nom = nom

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
        self.__background = Images().charger_image("res/img/interfaces/accueil/accueil-background.png")
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.MOUSEBUTTONUP, self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.__background, (-490, 0))
            image = Images().charger_image("res/img/interfaces/selection/joueur-1.png")
            ecran.blit(image, (20, 10))
            image = Images().charger_image("res/img/interfaces/selection/joueur-2.png")
            ecran.blit(image, (35, 435))
            image = Images().charger_image("res/img/interfaces/selection/zone-choix.png")
            ecran.blit(image, (40, 90))
            ecran.blit(image, (40, 515))
            image = Images().charger_image("res/img/interfaces/selection/esc-message.png")
            ecran.blit(image, (670, 3))
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
