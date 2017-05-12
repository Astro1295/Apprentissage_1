class personne:

    compteur_instance = 0

    def __init__(self, nom, prenom, age, messag1):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.message1 = messag1
        personne.compteur_instance +=1

    def messae_a_ecrire(self, message ):
        if self.nom != "":
            self.message1 = message

    def lire(self):
        print(self.message1)
    def effacer(self):
        self.message1 = ""
    def combien(cls):
        print("La il y eu {} instance de notre classe" .format(cls.compteur_instance))
    combien = classmethod(combien)

    def afficher():

        """Fonction chargée d'afficher quelque chose"""

        print("On affiche la même chose.")

        print("peu importe les données de l'objet ou de la classe.")

    afficher = staticmethod(afficher)


personne.combien()
personne.afficher()