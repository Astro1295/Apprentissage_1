import os
import pickle

path = "C:/Users/BQXP7653/git/Apprentissage_1"
current_dir = os.getcwd()
print(current_dir)
os.chdir(path)

print("****Bienvenue sur notre application de vente en ligne *****")
# deande d'information sur le user

sexe_user = input("Votre sexe H ou F ? ")
nom_user = input("C'est quoi votre nom ? \n")
prenom_user = input("C'est quoi votre prenom ? \n")
adresse_user = input("C'est quoi votre adresse ? \n")
age_user = input("Quel est votre age ? \n")

#traitement des information en base

sexe_user= sexe_user.lower()

if sexe_user == "h":
    sexe_user = "homme"
else:
    sexe_user = "femme"
# ecriture des infoamtion sur le fichier usr_info.txt
user_info ={"sexe":sexe_user,"nom":nom_user,"prenom":prenom_user,"adresse":adresse_user,"age":age_user}


fichier = open("path", "a")
for x,y in user_info.items():
    ecrire= fichier.write("{0}:{1}.\n" .format(x,y))
fichier.close()

fichier = open("path", "r")
source = fichier.read()
print(source)

mot = "bonjour"
if "b" in mot:
    print("youpi")