import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)

essai = 0
reponse = -1
win = False
while essai < 6:
    essai += 1
    i = int(input())
    if i == secret:
        print("Gagné en", essai, "essais !")
        win = True
        break
    if essai < 6:
        if i < secret:
            print("Trop petit")
        else:
            print("Trop grand")

if win == False:
    print("Perdu ! Le secret était", secret)

