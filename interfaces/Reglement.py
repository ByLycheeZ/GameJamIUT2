import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement
from gestionnaires.Images import Images

from utils import Constantes


class Reglement:
    TITRE = (48, 51, 107)  # Bleu marine
    SOUS_TITRE = (249, 202, 36)  # Jaune
    DESCRIPTION = (255, 255, 255)  # Blanc
    TOUCHE = (48, 51, 107)  # Bleu marine comme le titre

    def __init__(self, menu):
        self.montrer = False
        self.__menu = menu
        self.__background = Images().charger_image("res/img/interfaces/accueil/accueil-background.png")
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.__background, (0, 0))

            # Titre
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 60)
            texte = font.render("Règles", True, self.TITRE)
            ecran.blit(texte, (Constantes.LARGEUR / 2 - texte.get_width() / 2, 20))

            # Objectif
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
            ecran.blit(font.render("Objectif", True, self.SOUS_TITRE), (50, 110))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            ecran.blit(font.render("Soyez le dernier en vie en utilisant les", True, self.DESCRIPTION), (50, 160))
            ecran.blit(font.render("courants ascendants et descendants", True, (95, 39, 205)), (455, 160))
            ecran.blit(font.render("pour changer", True, self.DESCRIPTION), (860, 160))
            ecran.blit(font.render("d'étages. Vous disposez également d'une", True, self.DESCRIPTION), (50, 187))
            ecran.blit(font.render("compétence", True, (255, 165, 2)), (490, 187))
            ecran.blit(font.render("pour rééquilibrer le duel.", True, self.DESCRIPTION), (625, 187))
            ecran.blit(
                font.render("Evitez les obstacles et courez, la caméra se déplace en fonction du joueur en première",
                            True, self.DESCRIPTION), (50, 214))
            ecran.blit(
                font.render("position. Si vous sortez de l'écran (à gauche) vous perdez une vie et réapparaissez au",
                            True, self.DESCRIPTION), (50, 241))
            ecran.blit(font.render("centre de l'écran. Vous ne possédez que", True, self.DESCRIPTION), (50, 268))
            ecran.blit(font.render("3 vies", True, (231, 76, 60)), (485, 268))
            ecran.blit(font.render(".", True, self.DESCRIPTION), (550, 268))

            # Commandes
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
            ecran.blit(font.render("Commandes", True, self.SOUS_TITRE), (50, 320))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 26)
            ecran.blit(font.render("Joueur 1", True, self.DESCRIPTION), (350, 370))
            ecran.blit(font.render("Joueur 2", True, self.DESCRIPTION), (750, 370))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 22)
            ecran.blit(font.render("Déplacements", True, self.DESCRIPTION), (50, 480))
            ecran.blit(font.render("Compétence", True, self.DESCRIPTION), (50, 650))
            touche = Images().charger_image("res/img/interfaces/regles/touche.png")
            font = pygame.font.Font("res/fonts/NotoSansJP-Bold.otf", 45)

            # Joueur 1
            ecran.blit(touche, (370, 430))  # Haut
            ecran.blit(touche, (370, 505))  # Bas
            ecran.blit(touche, (290, 505))  # Gauche
            ecran.blit(touche, (450, 505))  # Droite
            ecran.blit(touche, (370, 630))  # Compétence
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['sauter']), True, self.TOUCHE), (390, 425))  # Haut
            # ecran.blit(font.render(pygame.key.name(Constantes.TOUCHES[0]['']), True, self.TOUCHE), (370, 505))  # Bas
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['aller_gauche']), True, self.TOUCHE), (307, 495))  # Gauche
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['accroupir']), True, self.TOUCHE), (390, 500))  # Accroupir
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['aller_droite']), True, self.TOUCHE), (470, 500))  # Droite
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['competence']), True, self.TOUCHE), (377, 630))  # Compétence

            # Joueur 2
            ecran.blit(touche, (770, 430))  # Haut
            ecran.blit(touche, (770, 505))  # Bas
            ecran.blit(touche, (690, 505))  # Gauche
            ecran.blit(touche, (850, 505))  # Droite
            ecran.blit(touche, (770, 630))  # Compétence
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['sauter']), True, self.TOUCHE), (785, 425))  # Haut
            # ecran.blit(font.render(pygame.key.name(Constantes.TOUCHES[0]['']), True, self.TOUCHE), (370, 505))  # Bas
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['aller_gauche']), True, self.TOUCHE), (700, 500))  # Gauche
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['accroupir']), True, self.TOUCHE), (785, 500))  # Accroupir
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['aller_droite']), True, self.TOUCHE), (865, 500))  # Droite
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['competence']), True, self.TOUCHE), (773, 627))  # Compétence

            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            texte = font.render("ESC pour retourner au menu principal", True, self.DESCRIPTION)
            ecran.blit(texte, (Constantes.LARGEUR / 2 - texte.get_width() / 2, 740))

    def evenement(self, evenement):
        if self.montrer and evenement.key == pygame.K_ESCAPE:
            self.montrer = False
            self.__menu.montrer = True

    def nom_touche(self, touche):
        touches = {
            pygame.K_RIGHT: '→',
            pygame.K_LEFT: '←',
            pygame.K_UP: '↑',
            pygame.K_DOWN: '↓',
            pygame.K_RSHIFT: 'R⇧',
            pygame.K_LSHIFT: 'L⇧'
        }
        if touche in touches.keys():
            return touches[touche]
        else:
            return pygame.key.name(touche).upper()
