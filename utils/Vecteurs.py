"""
classe Vecteur pour gerer les deplacements
"""


import math


class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def unite(self):
        norme = math.sqrt(self.x**2 + self.y**2)
        return Vecteur(self.x / norme, self.y / norme)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            return None
