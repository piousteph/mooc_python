from math import sqrt

le = input()

a = float(input())

if le not in ("T", "C", "O", "D", "I"):
    res = 'Polyèdre non connu'
else:
    if le == 'T':
        res = ( sqrt(2) / 12 ) * a ** 3
    if le == 'C':
        res = a ** 3
    if le == 'O':
        res = ( sqrt(2) / 3 ) * a ** 3
    if le == 'D':
        res = ( (15 + 7 * sqrt(5)) / 4 ) * a ** 3
    if le == 'I':
        res = ((5 * (3+sqrt(5))) / 12) * a ** 3

print(res)