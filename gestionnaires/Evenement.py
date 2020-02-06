class Evenement:
    class __Evenement:
        def __init__(self):
            self.__auditeurs = dict()
            self.__pause = None
            self.__maj = None
            self.__auditeurs_file = list()

        def enregistrer(self, evenement, objet):
            if self.__maj != evenement:
                if evenement not in self.__auditeurs.keys():
                    self.__auditeurs[evenement] = list()

                self.__auditeurs[evenement].append(objet)
            else:
                self.__auditeurs_file.append(objet)

        def supprimer(self, objet):
            for evenement in self.__auditeurs.keys():
                if objet in self.__auditeurs[evenement]:
                    self.__auditeurs[evenement].remove(objet)

        def maj(self, type_evenement, evenement):
            if self.__pause:
                self.__pause.evenement(evenement)
            else:
                self.__maj = type_evenement
                if type_evenement in self.__auditeurs.keys():
                    for classe in self.__auditeurs[type_evenement]:
                        classe.evenement(evenement)
                self.__maj = None
                self.__vider_file(type_evenement)

        def pause(self, objet):
            self.__pause = objet

        def reprendre(self):
            self.__pause = None

        def __vider_file(self, type_evenement):
            for auditeur in self.__auditeurs_file:
                self.__auditeurs[type_evenement].append(auditeur)

            self.__auditeurs_file.clear()

    __instance = None

    def __init__(self):
        if not Evenement.__instance:
            Evenement.__instance = Evenement.__Evenement()

    def enregistrer(self, evenement, objet):
        Evenement.__instance.enregistrer(evenement, objet)

    def supprimer(self, objet):
        Evenement.__instance.supprimer(objet)

    def maj(self, type_evenement, evenement):
        Evenement.__instance.maj(type_evenement, evenement)

    def pause(self, objet):
        Evenement.__instance.pause(objet)

    def reprendre(self):
        Evenement.__instance.reprendre()
