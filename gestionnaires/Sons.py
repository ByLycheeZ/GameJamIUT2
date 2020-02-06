import pygame


class Sons:
    class __Sons:
        def __init__(self):
            self.sons = dict()

        def jouer_musique(self, musique, extension, nb_boucle):
            if musique not in self.sons.keys():
                self.sons[musique] = pygame.mixer.Sound(f'res/sons/bgm/{musique}.{extension}')
            self.sons[musique].play(nb_boucle)

        def arreter_musique(self, musique):
            if musique in self.sons.keys():
                self.sons[musique].stop()

        def jouer_son(self, son, extension, loops, maxtime):
            pygame.mixer.Sound(f'res/sons/sfx/{son}.{extension}').play(loops, maxtime)

    __instance = None

    def __init__(self):
        if not Sons.__instance:
            Sons.__instance = Sons.__Sons()

    def jouer_musique(self, musique, extension='wav', nb_boucle=-1):
        self.__instance.jouer_musique(musique, extension, nb_boucle)

    def pause_musique(self, musique):
        self.__instance.arreter_musique(musique)

    def jouer_son(self, son, extension='wav', loops=0, maxtime=0):
        self.__instance.jouer_son(son, extension, loops, maxtime*1000)
