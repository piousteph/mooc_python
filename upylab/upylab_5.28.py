def placer_pion(couleur, colonne, grille):
    res = True
    for l in range(5, -1, -1):
        if grille[l][colonne] != 'V':
            break
    #print('C', colonne, 'L',l,'V',grille[l][colonne])
    if grille[l][colonne] != 'V' and l < 5:
        grille[l+1][colonne] = couleur
    elif l == 0 and grille[l][colonne] == 'V':
        grille[l][colonne] = couleur
    else:
        res = False
    return (res, grille)


# print(placer_pion("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))


# print(placer_pion("J", 4, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
#                      ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
#                      ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
#                      ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
#                      ['V', 'V', 'V', 'V', 'R', 'V', 'V']]))

print(placer_pion('R', 5, [['V', 'V', 'V', 'J', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))