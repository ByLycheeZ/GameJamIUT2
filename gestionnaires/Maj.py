class Maj:
    class __Maj:
        def __init__(self):
            self.__auditeurs = list()

        def enregistrer(self, objet):
            self.__auditeurs.append(objet)

        def supprimer(self, objet):
            if objet in self.__auditeurs:
                self.__auditeurs.remove(objet)

        def maj(self, delta):
            for classe in self.__auditeurs:
                classe.maj(delta)

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
