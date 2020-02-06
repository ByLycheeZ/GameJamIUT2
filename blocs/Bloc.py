import pygame
from gestionnaires.Affichage import *
from gestionnaires.Images import Images
from gestionnaires.Maj import *
import json

from utils.Animation import Animation


class Bloc:
    DESSINS = {}

    def __init__(self, nom_json, x, y, taille):
        fichier_json = open(f'res/blocs/{nom_json}.json')
        self.__donnees = json.load(fichier_json)
        self.__sprite = Images().charger_image('res/img/Tileset.png')
        self._x = x
        self._y = y
        self.__z = self.__donnees['z'] if 'z' in self.__donnees.keys() else 0
        self.__taille = taille
        self._dessin = None
        self.__animation = None

        if all(cle in self.__donnees for cle in ['animation', 'temps-animation']):
            self.__animation = Animation(self.__donnees['x'], self.__donnees['y'], self.__donnees['largeur'],
                                         self.__donnees['hauteur'], self.__donnees['animation'],
                                         self.__donnees['temps-animation'])
            direction = self.__donnees['direction']
            if direction == 'x':
                self.__direction = [1, 0]
                self.__largeur = self.__donnees['largeur'] * taille
                self.__hauteur = self.__donnees['hauteur']
            else:
                self.__direction = [0, 1]
                self.__largeur = self.__donnees['largeur']
                self.__hauteur = self.__donnees['hauteur'] * taille
            Maj().enregistrer(self)
        else:
            fin_debut = 0
            fin_milieu = 0
            taille_milieu = 0

            if self.__donnees['direction'] == 'x':
                largeur = 0
                for debut in self.__donnees['debut']:
                    largeur += debut['largeur']
                fin_debut = largeur
                for milieu in self.__donnees['milieu']:
                    taille_milieu += milieu['largeur']
                largeur += taille_milieu * self.__taille
                fin_milieu = largeur
                for fin in self.__donnees['fin']:
                    largeur += fin['largeur']

                hauteur = self.__donnees['debut'][0]['hauteur']
            elif self.__donnees['direction'] == 'y':
                largeur = self.__donnees['debut'][0]['largeur']

                hauteur = 0
                for debut in self.__donnees['debut']:
                    hauteur += debut['hauteur']
                fin_debut = largeur
                for milieu in self.__donnees['milieu']:
                    taille_milieu += milieu['hauteur']
                    hauteur += taille_milieu * self.__taille
                    fin_milieu = largeur
                for fin in self.__donnees['fin']:
                    hauteur += fin['hauteur']
            else:
                largeur = self.__donnees['debut'][0]['largeur']
                hauteur = self.__donnees['debut'][0]['hauteur']

            self.__taille = taille
            nom_cache = f'{nom_json}|{taille}'
            if nom_cache not in Bloc.DESSINS:
                self.__init_dessin(largeur, hauteur, fin_debut, fin_milieu, taille_milieu)
                Bloc.DESSINS[nom_cache] = self._dessin
            else:
                self._dessin = Bloc.DESSINS[nom_cache]
            self.__largeur = self._dessin.get_width()

        Affichage().enregistrer(self, self.__z)

    def dessiner_partie(self, direction, decalage, partie):
        for element in partie:
            sprite = self.__sprite.subsurface(
                pygame.Rect(element['x'], element['y'], element['largeur'], element['hauteur']))
            x_element = element['dx'] + direction[0] * decalage
            y_element = element['dy'] + direction[1] * decalage
            self._dessin.blit(sprite, (x_element, y_element))

    def __init_dessin(self, largeur, hauteur, fin_debut, fin_milieu, taille_milieu):
        self._dessin = pygame.Surface((largeur, hauteur)).convert_alpha()
        self._dessin.fill((0, 0, 0, 0))

        direction = [0, 0]
        if self.__donnees['direction'] == 'x':
            direction[0] = 1
        elif self.__donnees['direction'] == 'y':
            direction[1] = 1

        self.dessiner_partie(direction, 0, self.__donnees['debut'])
        for i in range(0, self.__taille):
            self.dessiner_partie(direction, fin_debut + taille_milieu * i, self.__donnees['milieu'])
        self.dessiner_partie(direction, fin_milieu, self.__donnees['fin'])

    def maj(self, delta):
        self.__animation.ajouter_temps(delta)

    def affichage(self, ecran):
        if self.__animation:
            for i in range(self.__taille):
                x = self._x + (self.__donnees['largeur'] * i) * self.__direction[0]
                y = self._y + (self.__donnees['hauteur'] * i) * self.__direction[1]
                sous_sprite, sous_sprite_rect = self.__animation.recuperer_sous_sprite(self.__sprite, x, y)
                ecran.blit(sous_sprite, sous_sprite_rect)
        else:
            ecran.blit(self._dessin, (self._x, self._y))

        this_rect = self.get_rect()
        this_rect.x, this_rect.y = self._x, self._y
        pygame.draw.rect(ecran, (0, 0, 0), this_rect, 2)

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_largeur(self):
        return self.__largeur

    def get_rect(self):
        if self._dessin:
            return self._dessin.get_rect()
        else:
            return pygame.rect.Rect(self._x, self._y, self.__largeur, self.__hauteur)

    def collisions(self, joueur, delta):
        return None
