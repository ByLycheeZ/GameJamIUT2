class Affichage:
    class __Affichage:
        def __init__(self):
            self.__auditeurs = list()

        def enregistrer(self, classe):
            self.__auditeurs.append(classe)

        def affichage(self, ecran):
            for classe in self.__auditeurs:
                classe.affichage(ecran)

    __instance = None

    def __init__(self):
        if not Affichage.__instance:
            Affichage.__instance = Affichage.__Affichage()

    def enregistrer(self, classe):
        Affichage.__instance.enregistrer(classe)

    def maj(self, ecran):
        Affichage.__instance.affichage(ecran)
