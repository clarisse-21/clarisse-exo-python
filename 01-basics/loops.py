nombre=int(input("Entrez un nombre : "))
N=nombre+1
somme=0
for i in range(1,N):
    somme = somme + i
print (somme)

table=int(input("Entrez un nombre : "))
for y in range (1,11):
    print (f" {table}  x  {y}  =  {table*y}")