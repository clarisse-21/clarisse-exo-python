liste=[4,1,7,3,18,14]
max=0
for valeur in liste :
    if valeur > max :
        max=valeur
print (max)

somme=0
for valeur in liste :
    somme = somme+valeur
moyenne = somme/len(liste)
print(moyenne)

compteur = 0

for valeur in liste :
    if valeur>moyenne :
        compteur = compteur + 1
print(compteur)