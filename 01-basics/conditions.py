nombre=int(input("Entrez un nombre : "))
if nombre%2==0 :
    print(f"{nombre} est pair")
else :
    print(f"{nombre} est impair")

age=int(input("Entrez votre âge : "))

if age<=12 :
    print("catégorie enfant")
elif age >12 and age <=17 :
    print("catégorie adolescent")
elif age >17 and age<=64 :
    print("catégorie adulte")
else : 
    print("catégorie sénior")