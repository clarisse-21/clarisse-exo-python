mot=input("Entrez un mot : ")
compteur=0
for lettre in mot:
    if lettre in "aeiouy":
        compteur = compteur+1
print (compteur)

phrase=input("Entrez une phrase : ")
nbmot=phrase.split(" ")
print(len(nbmot))
long=[]
for mot2 in nbmot :
    if len(mot2)>len(long) :
        long=mot2
print (long)

