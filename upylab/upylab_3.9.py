initiale = int(input())
cible = int(input())

courante = initiale
first = 1

while (courante != initiale and courante != cible) or first == 1:
    first = 0
    print(courante)
    courante = (courante + initiale) % 100

if (courante == cible):
    print("Cible atteinte")
else:
    print("Pas trouvé")
