import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
import json


class Bloc:

    def __init__(self, nom_json, x, y, taille):
        fichier_json = open(f'res/blocs/{nom_json}.json')
        self.donnees = json.load(fichier_json)
        self.sprite = pygame.image.load('res/blocs/Tileset.png')
        self.x = x
        self.y = y

        fin_debut = 0
        fin_milieu = 0
        taille_milieu = 0

        if self.donnees['direction'] == 'x':
            largeur = 0
            for debut in self.donnees['debut']:
                largeur += debut['largeur']
            fin_debut = largeur
            for milieu in self.donnees['milieu']:
                taille_milieu += milieu['largeur']
            largeur += taille_milieu * taille
            fin_milieu = largeur
            for fin in self.donnees['fin']:
                largeur += fin['largeur']

            hauteur = self.donnees['debut'][0]['hauteur']
        elif self.donnees['direction'] == 'y':
            largeur = self.donnees['debut'][0]['largeur']

            hauteur = 0
            for debut in self.donnees['debut']:
                hauteur += debut['hauteur']
            fin_debut = largeur
            for milieu in self.donnees['milieu']:
                taille_milieu += milieu['hauteur']
                hauteur += taille_milieu * taille
                fin_milieu = largeur
            for fin in self.donnees['fin']:
                hauteur += fin['hauteur']
        else:
            largeur = self.donnees['debut'][0]['largeur']
            hauteur = self.donnees['debut'][0]['hauteur']

        self.taille = taille
        self.init_dessin(largeur, hauteur, fin_debut, fin_milieu, taille_milieu)

        Affichage().enregistrer(self)

    def dessiner_partie(self, direction, decalage, partie):
        for element in partie:
            sprite = self.sprite.subsurface(pygame.Rect(element['x'], element['y'], element['largeur'], element['hauteur']))
            x_element = element['dx'] + direction[0] * decalage
            y_element = element['dy'] + direction[1] * decalage
            self.dessin.blit(sprite, (x_element, y_element))

    def init_dessin(self, largeur, hauteur, fin_debut, fin_milieu, taille_milieu):
        self.dessin = pygame.Surface((largeur, hauteur)).convert_alpha()
        self.dessin.fill((0, 0, 0, 0))

        direction = [0, 0]
        if self.donnees['direction'] == 'x':
            direction[0] = 1
        elif self.donnees['direction'] == 'y':
            direction[1] = 1

        self.dessiner_partie(direction, 0, self.donnees['debut'])
        for i in range(0, self.taille):
            self.dessiner_partie(direction, fin_debut + taille_milieu * i, self.donnees['milieu'])
        self.dessiner_partie(direction, fin_milieu, self.donnees['fin'])


    def affichage(self, ecran):
        ecran.blit(self.dessin, (self.x, self.y))

#


        # Cas du else à voir
