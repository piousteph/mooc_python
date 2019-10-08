import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

point = 0

def check(o, j):
    res = ""
    if o == PIERRE and j == CISEAUX:
        res = ("Pierre bat Ciseaux", -1)
    elif o == CISEAUX and j == FEUILLE:
        res = ("Ciseaux bat Feuille", -1)
    elif o == FEUILLE and j == PIERRE:
        res = ("Feuille bat Pierre", -1)
    
    elif j == PIERRE and o == CISEAUX:
        res = ("Ciseaux est battu par Pierre", 1)
    elif j == CISEAUX and o == FEUILLE:
        res = ("Feuille est battu par Ciseaux", 1)
    elif j == FEUILLE and o == PIERRE:
        res = ("Pierre est battu par Feuille", 1)

    elif j == PIERRE and o == PIERRE:
        res = ("Pierre annule Pierre", 0)
    elif j == FEUILLE and o == FEUILLE:
        res = ("Feuille annule Feuille", 0)
    elif j == CISEAUX and o == CISEAUX:
        res = ("Ciseaux annule Ciseaux", 0)
    return res

def manche(point):
    o = random.randint(0, 2)
    j = int(input())

    res = check(o, j)
    point += res[1]
    print(res[0], ':', point)
    return point

s = int(input())
random.seed(s)

for i in range(5):
    point = manche(point)

if point > 0:
    print("Gagné")
elif point < 0:
    print("Perdu")
else:
    print("Nul")