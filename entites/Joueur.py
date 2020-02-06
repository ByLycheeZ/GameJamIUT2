import pygame
import gestionnaires.Jeu as Jeu
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from gestionnaires.Evenement import *
from gestionnaires.Sons import Sons
from utils.Animation import Animation
from utils.Constantes import CHEMIN_SPRITE, HAUTEUR, TAILLE_PERSO
from decorations.Parallax import Parallax
from interfaces.Ecran import Ecran
from interfaces.hud.HudVie import HudVie


class Joueur:
    NB_SAUT_MAX = 1
    RECTANGLE_COLLISION = pygame.Rect(20, 20, 75, 85)
    TEMPS_SUBIT_TORNADE = 2  # En seconde

    __count = 0

    def __init__(self, touches, couleur):
        # Private
        Joueur.__count += 1
        self.__vies = 1
        self.__sprite = pygame.image.load(f'{CHEMIN_SPRITE}dino-{couleur}.png')
        self.__hud = HudVie(self.__vies, couleur)
        self.__rect = self.__sprite.get_rect()
        self.__rect.y = HAUTEUR - TAILLE_PERSO[1]
        self.__vitesse = 300
        self.__deplacement = [0, 0]
        self.__velocite_saut, self.vitesse_chute = 2, 4
        self.__nb_saut_restant = 1
        self._subit_tornade = -1
        self.__anim_attente = Animation(0, 0, TAILLE_PERSO[0], TAILLE_PERSO[1], 4, 0.2)
        self.__anim_deplacement = Animation(4, 0, TAILLE_PERSO[0], TAILLE_PERSO[1], 6, 0.2)
        self.__anim_attaque = Animation(10, 0, TAILLE_PERSO[0], TAILLE_PERSO[1], 3, 0.2)
        self.__anim_degat = Animation(13, 0, TAILLE_PERSO[0], TAILLE_PERSO[1], 4, 0.2)
        self.__anim_accroupi = Animation(18, 0, TAILLE_PERSO[0], TAILLE_PERSO[1], 6, 0.2)
        self.__anim_active = self.__anim_attente

        # Protected
        self._touches = touches
        self._couleur = couleur

        evenement = Evenement()
        evenement.enregistrer(pygame.KEYDOWN, self)
        evenement.enregistrer(pygame.KEYUP, self)
        Affichage().enregistrer(self, 1)
        Maj().enregistrer(self)

    def evenement(self, evenement):
        if self.__vies <= 0:
            return

        if evenement.type == pygame.KEYDOWN:
            if evenement.key == self._touches.get('aller_gauche'):
                self.__deplacement[0] -= 1
            elif evenement.key == self._touches.get('aller_droite'):
                self.__deplacement[0] += 1
            elif evenement.key == self._touches.get('sauter') and self.__nb_saut_restant > 0:
                self.__deplacement[1] -= self.__velocite_saut
                self.__nb_saut_restant -= 1

        else:  # KEYUP
            if evenement.key == self._touches.get('aller_gauche'):
                self.__deplacement[0] += 1
            elif evenement.key == self._touches.get('aller_droite'):
                self.__deplacement[0] -= 1

        if self.__deplacement[0] != 0:
            self.__anim_active = self.__anim_deplacement
        else:
            self.__anim_active = self.__anim_attente

    def maj(self, delta):
        jeu = Jeu.Jeu()
        if self.__vies <= 0:
            return
        elif Joueur.__count == 1:
            jeu.fin(self._couleur)
            return

        if self._subit_tornade <= 0:
            self.__anim_active.ajouter_temps(delta)

            # Mouvement X
            self.__rect = self.__rect.move(self.__vitesse * self.__deplacement[0] * delta, 0)
            self.__collisions((self.__deplacement[0], 0), jeu.collisions(self, 0))

            # Mouvement Y
            self.__rect = self.__rect.move(0, self.__vitesse * self.__deplacement[1] * delta)
            self.__collisions((0, self.__deplacement[1]), jeu.collisions(self, delta))

            self.__deplacement[1] += self.vitesse_chute * delta
        else:
            # gere temps de stun
            self._subit_tornade -= delta

        self.__maj_camera(delta)

    def __collisions(self, deplacement, collisions):
        if collisions:
            rect = self.get_rect_collision()
            if deplacement[0] > 0:
                rect.right = collisions.left
            elif deplacement[0] < 0:
                rect.left = collisions.right

            if deplacement[1] < 0:
                rect.top = collisions.bottom
                self.__deplacement[1] = 0
            elif deplacement[1] > 0:
                rect.bottom = collisions.top
                self.__deplacement[1] = 0
                self.ajout_saut(1)
            self.set_rect_collision(rect)

    def __maj_camera(self, delta):
        droite = self.__rect.left + TAILLE_PERSO[0]
        if Ecran.get_droite() - droite < 10:
            Ecran.deplacement(droite - Ecran.largeur + 10, Ecran.y)
            Parallax().deplacement_joueur(self.__deplacement[0], delta)

        if Ecran.x > droite:
            self.__retirer_vie()

    def __retirer_vie(self):
        self.__vies -= 1
        self.__hud.retirer_pv()

        if Jeu.Jeu.konami_actif():
            Sons().jouer_son('k-mort')
        else:
            Sons().jouer_son('mort')

        if self.__vies > 0:
            self.__revivre()
        else:
            Joueur.__count -= 1

    def __revivre(self):
        self.__rect.x = Ecran.x + Ecran.largeur / 2

    def affichage(self, ecran):
        if self.__vies <= 0:
            return

        sous_sprite, sous_sprite_rect = self.__anim_active.recuperer_sous_sprite(self.__sprite, self.__rect.x,
                                                                                 self.__rect.y)
        ecran.blit(pygame.transform.flip(sous_sprite, self.__deplacement[0] < 0, False), sous_sprite_rect)

    def get_couleur(self):
        return self._couleur

    def get_vitesse(self):
        return self.__vitesse

    def get_sprite(self):
        return self.__sprite

    def get_rect(self):
        return self.__rect

    def get_rect_collision(self):
        rect = self.__rect.copy()
        rect.x += self.RECTANGLE_COLLISION.x
        rect.y += self.RECTANGLE_COLLISION.y
        rect.width = self.RECTANGLE_COLLISION.width
        rect.height = self.RECTANGLE_COLLISION.height
        return rect

    def set_rect_collision(self, rect):
        self.__rect.x = rect.x - self.RECTANGLE_COLLISION.x
        self.__rect.y = rect.y - self.RECTANGLE_COLLISION.y

    def get_deplacement(self):
        return self.__deplacement

    def get_nb_saut_restant(self):
        return self.__nb_saut_restant

    def get_nb_saut_max(self):
        return self.NB_SAUT_MAX

    def set_vitesse(self, vitesse):
        self.__vitesse = vitesse

    def set_deplacement(self, deplacement):
        self.__deplacement = deplacement

    def set_sprite(self, nom_fichier):
        self.__sprite = pygame.image.load(CHEMIN_SPRITE + nom_fichier)

    def set_rect(self, rect):
        self.__rect = rect

    def set_velocite_saut(self, velocite_saut):
        self.__velocite_saut = velocite_saut

    def set_vitesse_chute(self, vitesse_chute):
        self.vitesse_chute = vitesse_chute

    def ajout_saut(self, nb=1):
        self.__nb_saut_restant = min([nb + self.__nb_saut_restant, self.NB_SAUT_MAX])

    def fin(self):
        self.__hud.fin()
        Joueur.__count = 0
        Evenement().supprimer(self)
        Affichage().supprimer(self)
        Maj().supprimer(self)

    def subit_tornade(self):
        self._subit_tornade = self.TEMPS_SUBIT_TORNADE