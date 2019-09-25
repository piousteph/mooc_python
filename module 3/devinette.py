import random

secret = random.randint(0, 5)

choix = int(input())

if choix == secret:
    print("GAGNE")
else:
    print("PERDU, la valeur secrete etait ", secret)