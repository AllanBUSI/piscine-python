# Recherche du plus grand nombre:
# Écrivez un programme qui prend trois nombres en entrée et affiche le plus grand.

num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))
num3 = float(input("Entrez le troisième nombre : "))
maximum = max(num1, num2, num3)
print("Le plus grand nombre est :", maximum)