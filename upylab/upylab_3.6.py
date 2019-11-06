mise = 10
pari = int(input())
tirage = int(input())

res = 0

if pari == tirage:
    res = mise * 12
elif pari == 13 and tirage % 2 == 0:
    res = mise * 2
elif pari == 14 and tirage % 2 != 0:
    res = mise * 2
elif pari == 15 and tirage in (1, 3, 5, 7, 9, 12):
    res = mise * 2
elif pari == 16 and tirage in (2, 4, 6, 8, 10, 11):
    res = mise * 2
print(res)