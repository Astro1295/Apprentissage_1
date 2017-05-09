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

print(afficher_flottant(12.2222222))
ma_list = [1,2,4,5,2]

ma_list.sort()

ma_liste1 = sorted(ma_list)

print(ma_list)
print(ma_liste1)
