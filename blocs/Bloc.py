import pygame
from gestionnaires.Affichage import *
import json


class Bloc:
    def __init__(self, nom_json, x, y, taille):
        fichier_json = open(f'res/blocs/{nom_json}.json')
        self.__donnees = json.load(fichier_json)
        self.__sprite = pygame.image.load('res/img/Tileset.png')
        self.__x = x
        self.__y = y

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
            largeur += taille_milieu * taille
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
                hauteur += taille_milieu * taille
                fin_milieu = largeur
            for fin in self.__donnees['fin']:
                hauteur += fin['hauteur']
        else:
            largeur = self.__donnees['debut'][0]['largeur']
            hauteur = self.__donnees['debut'][0]['hauteur']

        self.__taille = taille
        self.__init_dessin(largeur, hauteur, fin_debut, fin_milieu, taille_milieu)

        Affichage().enregistrer(self)

    def dessiner_partie(self, direction, decalage, partie):
        for element in partie:
            sprite = self.__sprite.subsurface(
                pygame.Rect(element['x'], element['y'], element['largeur'], element['hauteur']))
            x_element = element['dx'] + direction[0] * decalage
            y_element = element['dy'] + direction[1] * decalage
            self.__dessin.blit(sprite, (x_element, y_element))

    def __init_dessin(self, largeur, hauteur, fin_debut, fin_milieu, taille_milieu):
        self.__dessin = pygame.Surface((largeur, hauteur)).convert_alpha()
        self.__dessin.fill((0, 0, 0, 0))

        direction = [0, 0]
        if self.__donnees['direction'] == 'x':
            direction[0] = 1
        elif self.__donnees['direction'] == 'y':
            direction[1] = 1

        self.dessiner_partie(direction, 0, self.__donnees['debut'])
        for i in range(0, self.__taille):
            self.dessiner_partie(direction, fin_debut + taille_milieu * i, self.__donnees['milieu'])
        self.dessiner_partie(direction, fin_milieu, self.__donnees['fin'])

    def affichage(self, ecran):
        ecran.blit(self.__dessin, (self.__x, self.__y))
