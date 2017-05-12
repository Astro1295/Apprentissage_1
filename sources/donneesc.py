"""Ce fichier définit quelques données, sous la forme de variables,
utiles au programme pendu"""

# Nombre de coups par partie
nb_coups = 8

# Nom du fichier stockant les scores
nom_fichier_scores = "scores.txt"

# Liste des mots du pendu
liste_mots = [
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]


ma_liste = [1, 2, 4, 8, 16, 32, 64,12,11,5,4]
ma_liste = [n for n in ma_liste if n < 16]
print(ma_liste)

