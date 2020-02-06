import pygame


class Images:
    class __Images:
        def __init__(self):
            self.__images = dict()

        def charger_image(self, chemin):
            if chemin not in self.__images.keys():
                self.__images[chemin] = pygame.image.load(chemin)
            return self.__images[chemin]

    __instance = None

    def __init__(self):
        if not Images.__instance:
            Images.__instance = Images.__Images()

    def charger_image(self, chemin):
        return self.__instance.charger_image(chemin)
