# Vérification de nombre pair ou impair:
# Écrivez un programme qui vérifie si un nombre donné par l'utilisateur est pair ou impair.
nombre = int(input("Entrez un nombre : "))
if nombre % 2 == 0:
    print(nombre, "est pair.")
else:
    print(nombre, "est impair.")