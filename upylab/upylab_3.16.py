i = int(input())

for x in range(i):
    ch = ''
    nbspace = ' ' * (i - x - 1)
    for y in range((x + x) // 2 ):
        ch += str(x + y)[-1:]
    for y in range((x + x) // 2 ):
        ch += str(x + y)[-1:]
    
    print(nbspace + ch)