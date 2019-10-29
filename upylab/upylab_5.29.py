def check(x, y, dir_x, dir_y, grille):
    res = ''

    found = 1
    val = grille[x][y]
    print('Checking for ',val, 'at', x, y, 'with', dir_x, dir_y)

    while x >= 0 and x < 5 and y >= 0 and y < 6:
        x = x + dir_x
        y = y + dir_y
        if grille[x][y] == val:
            print('next check', x, y)
            found += 1
            if found == 4:
                res = val
                break
        else:
            break

    return res

def gagnant(grille):
    res = None
    dir = [
        [1, 0], 
        [1, 1],
        [0, 1],
        [-1, 1],
        [-1, 0],
        [-1, -1],
        [0, -1],
        [1, -1]
    ]
    for l in range(len(grille)):
        for c in range(len(grille[l])):
            if grille[l][c] != 'V':
                for d in range(8):
                    if check(l,c,dir[d][0],dir[d][1],grille) != '': 
                        res = grille[l][c]
                        break
            if res != None:
                break
        if res != None:
            break
    return res



print(gagnant([
    ['V', 'V', 'V', 'J', 'R', 'R', 'J'],
    ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
    ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
