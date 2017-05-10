import os
from random import randrange, choice
from sources import donnees


def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.


    De plus, on va remplacer le point décimal par la virgule"""

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")

    flottant = str(flottant)

    partie_entiere, partie_flottante = flottant.split(".")

    # La partie entière n'est pas à modifier

    # Seule la partie flottante doit être tronquée

    return ",".join([partie_entiere, partie_flottante[:3]])

# focntion pour recherche mot lettre dans un mot

def recherche_lettre(mot, lettre):
    mot = str(mot).lower()
    lettre = str(lettre).lower()

    if lettre in mot:
        return True
    else:
        print("\n ** La lettre n'est pas présente dans notre mot **!!\n ")

def recherche_mot_liste(lettre):
    lettre = str(lettre).lower()
    coups_user = donnees.nb_coups
# vérification si la lettre est dans le mot
    if recherche_lettre(choice(donnees.mon_mot), lettre):
        print("\n Bravo la lettre est dans le mot choisi !!")
        donnees.scores_user+=1
    else:
        coups_user-=1
        print("\n Essayes une seconde fois ! il te reste que ", coups_user, "à jouer !!")

def demande_nom():
    nom = input("\n C'est quoi votre nom ? \n")
    if len(nom) < 4 or not nom.isalpha():
        print("Le nom est incorrect !!! Saisissez un nouveau ")
        return demande_nom()
    else:
        return nom

def demande_lettre():
    lettre = input("\n C'est quoi votre choix de lettre ? \n")
    lettre = lettre.lower()
    if len(lettre) > 1 or not lettre.isalpha():
        print("La lettre est incorrecte !!! ")
        return demande_lettre()
    else:
        return lettre


