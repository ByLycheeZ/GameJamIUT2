from decorations.CoucheParallax import CoucheParallax


class Parallax:
    class __Parallax:
        def __init__(self):
            self.parallax = list()

            for i in range(2, 10):
                self.parallax.append(CoucheParallax(i, 250 - 20 * i, 1.0))

            # self.parallax.append(CoucheParallax(1, 20, 0.7))

        def deplacement_joueur(self, direction, delta):
            for parallax in self.parallax:
                parallax.deplacement(direction, delta)

    __instance = None

    def __init__(self):
        if not Parallax.__instance:
            Parallax.__instance = Parallax.__Parallax()

    def deplacement_joueur(self, direction, delta):
        self.__instance.deplacement_joueur(direction, delta)
