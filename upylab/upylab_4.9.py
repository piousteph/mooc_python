def bat(j1, j2):
    if j1 == 0 and j2 == 2:
        res = True
    elif j1 == 1 and j2 == 0:
        res = True
    elif j1 == 2 and j2 == 1:
        res = True
    else:
        res = False
    return res

print(bat(0,0))
print(bat(0,1))
print(bat(2,1))
