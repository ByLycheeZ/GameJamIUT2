class Affichage:
    class __Affichage:
        def __init__(self):
            self.__auditeurs = dict()

        def enregistrer(self, objet, couche):
            if couche not in self.__auditeurs.keys():
                self.__auditeurs[couche] = list()

            self.__auditeurs[couche].append(objet)

        def supprimer(self, objet):
            for couche in self.__auditeurs.keys():
                if objet in self.__auditeurs[couche]:
                    self.__auditeurs[couche].remove(objet)

        def affichage(self, ecran):
            for couche in sorted(self.__auditeurs):
                for classe in self.__auditeurs[couche]:
                    classe.affichage(ecran)

    __instance = None

    def __init__(self):
        if not Affichage.__instance:
            Affichage.__instance = Affichage.__Affichage()

    def enregistrer(self, objet, couche=0):
        Affichage.__instance.enregistrer(objet, couche)

    def supprimer(self, objet):
        Affichage.__instance.supprimer(objet)

    def maj(self, ecran):
        Affichage.__instance.affichage(ecran)
