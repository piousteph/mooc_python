import random

def alea_dice(s):
    random.seed(s)

    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)

    res = False

    if d1 == 4 and d2 == 2 and d3 == 1:
        res = True
    elif d1 == 4 and d2 == 1 and d3 == 2:
        res = True
    elif d1 == 2 and d2 == 4 and d3 == 1:
        res = True
    elif d1 == 2 and d2 == 1 and d3 == 4:
        res = True
    elif d1 == 1 and d2 == 4 and d3 == 2:
        res = True
    elif d1 == 1 and d2 == 2 and d3 == 4:
        res = True
    else:
        res = False    
    return res

print(alea_dice(1))
