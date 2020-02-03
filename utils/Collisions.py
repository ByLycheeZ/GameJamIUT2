"""
classe Collision pour gerer les collisions entre des objets
"""

class Collisions:

    @staticmethod
    def rect_collision(x_a, y_a, largeur_a, hauteur_a, x_b, y_b, largeur_b, hauteur_b):
        return x_a < x_b + largeur_b and x_a + largeur_a > x_b and y_a > y_b + hauteur_b and y_a + hauteur_a < y_b

    @staticmethod
    def rect_collision(rect_a, x_b, y_b, largeur_b, hauteur_b):
        return Collisions.rect_collision(rect_a.x, rect_a.y, rect_a.width, rect_a.height, x_b, y_b, largeur_b, hauteur_b)

    @staticmethod
    def rect_collision(rect_a, rect_b):
        return Collisions.rect_collision(rect_a, rect_b.x, rect_b.y, rect_b.width, rect_b.height)
