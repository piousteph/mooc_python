import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)

essai = 0
reponse = -1

while essai != 6 and reponse != secret:
    essai += 1
    i = int(input())
    if i < secret:
        print("Trop petit")
    elif i > secret:
        print("Trop grand")
    else:
        print("Gagné en", essai, "essais !")
if (essai == 6):
    print("Perdu ! Le secret était", secret)