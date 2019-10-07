def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    res = True
    if n < 2:
        res = False
    for x in range(2, n):
        if (n % x) == 0:
            res = False
    return res

# code principal
n = int(input())

for i in range(2, n+1):
    if premier(i):
        print(i)