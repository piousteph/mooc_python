from math import sqrt

a = float(input())
b = float(input())

if a < 0 or b < 0:
    print('Erreur')
else:
    print(sqrt(a*b))