class Affichage:
    class __Affichage:
        def __init__(self):
            self.__auditeurs = dict()

        def enregistrer(self, classe, couche):
            if couche not in self.__auditeurs.keys():
                self.__auditeurs[couche] = list()

            self.__auditeurs[couche].append(classe)

        def affichage(self, ecran):
            for couche in sorted(self.__auditeurs):
                for classe in self.__auditeurs[couche]:
                    classe.affichage(ecran)

    __instance = None

    def __init__(self):
        if not Affichage.__instance:
            Affichage.__instance = Affichage.__Affichage()

    def enregistrer(self, classe, couche=0):
        Affichage.__instance.enregistrer(classe, couche)

    def maj(self, ecran):
        Affichage.__instance.affichage(ecran)
