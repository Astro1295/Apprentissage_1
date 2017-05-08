import os
from Fonction.Fonctions import operation, random_number, pair_impair, Casino

print("********************Bienvenue sur notre application Casino****************")

demande = input("Choisi un chifffre entre 0 et 49")
Somme   = input("Entrez une somme à miser")

demande = int(demande)
Somme = int(Somme)

Casino(Somme, demande)


