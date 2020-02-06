from gestionnaires.Affichage import Affichage
from gestionnaires.Images import Images
from gestionnaires.Maj import Maj
from utils.Constantes import HAUTEUR


class HudFlecheDirection:
    def __init__(self):
        self.__fleche = Images().charger_image('res/img/fleche.png')
        self.__visible = True
        self.__temps = 0
        self.__delai = 0.5

        Affichage().enregistrer(self, 5)
        Maj().enregistrer(self)

    def maj(self, delta):
        self.__temps += delta
        if self.__temps >= self.__delai:
            self.__temps -= self.__delai
            self.__visible = not self.__visible

    def affichage(self, ecran):
        if self.__visible:
            ecran.blit(self.__fleche, (10, HAUTEUR / 2 - self.__fleche.get_rect().height / 2))

    def fin(self):
        Affichage().supprimer(self)
        Maj().supprimer(self)
