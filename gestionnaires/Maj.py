class Maj:
    class __Maj:
        def __init__(self):
            self.__auditeurs = list()

        def enregistrer(self, classe):
            self.__auditeurs.append(classe)

        def maj(self, delta):
            for classe in self.__auditeurs:
                classe.maj(delta)

    __instance = None

    def __init__(self):
        if not Maj.__instance:
            Maj.__instance = Maj.__Maj()

    def enregistrer(self, classe):
        Maj.__instance.enregistrer(classe)

    def maj(self, delta):
        Maj.__instance.maj(delta)