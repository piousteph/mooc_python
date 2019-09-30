res = 0
i = 0

nb = int(input())

if nb == -1:
    while i != 'F':
        i = input()
        if i != 'F':
            res += int(i)
else:
    for x in range(nb):
        i = int(input())
        res += i
print(res)