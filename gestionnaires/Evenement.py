class Evenement:
    class __Evenement:
        def __init__(self):
            self.__auditeurs = dict()

        def enregistrer(self, evenement, classe):

            if evenement not in self.__auditeurs.keys():
                self.__auditeurs[evenement] = list()

            self.__auditeurs[evenement].append(classe)

        def maj(self, type_evenement, evenement):
            if type_evenement in self.__auditeurs.keys():
                for classe in self.__auditeurs[type_evenement]:
                    classe.evenement(evenement)

    __instance = None

    def __init__(self):
        if not Evenement.__instance:
            Evenement.__instance = Evenement.__Evenement()

    def enregistrer(self, evenement, classe):
        Evenement.__instance.enregistrer(evenement, classe)

    def maj(self, type_evenement, evenement):
        Evenement.__instance.maj(type_evenement, evenement)