chaine = "AMIROUCHE"
chaine = chaine.lower()
print(chaine)

nom = "rahani"
prenom = "amirouche"

print("je suis monsieur {0}  {1}".format(prenom, nom))

info = """{nom},{prenom},{adresse},({pays})""".format(nom= "RAHANI", prenom ="Amirouche", adresse = "5 rue des aubevoys, 85800 Cergy", pays = "France")
print(info)

ma_list = ["1", "2"]
ma_list.append(3)
print(ma_list.__len__())