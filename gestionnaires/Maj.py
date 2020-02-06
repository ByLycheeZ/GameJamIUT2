class Maj:
    class __Maj:
        def __init__(self):
            self.__auditeurs = list()
            self.__pause = None

        def enregistrer(self, objet):
            self.__auditeurs.append(objet)

        def supprimer(self, objet):
            if objet in self.__auditeurs:
                self.__auditeurs.remove(objet)

        def maj(self, delta):
            if not self.__pause:
                for classe in self.__auditeurs:
                    classe.maj(delta)

        def pause(self, objet):
            self.__pause = objet

        def reprendre(self):
            self.__pause = None

    __instance = None

    def __init__(self):
        if not Maj.__instance:
            Maj.__instance = Maj.__Maj()

    def enregistrer(self, objet):
        Maj.__instance.enregistrer(objet)

    def supprimer(self, objet):
        Maj.__instance.supprimer(objet)

    def maj(self, delta):
        Maj.__instance.maj(delta)

    def pause(self, objet):
        Maj.__instance.pause(objet)

    def reprendre(self):
        Maj.__instance.reprendre()
