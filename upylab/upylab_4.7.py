def rendre_monnaie(prix, x20, x10, x5, x2, x1):

    res = tuple()
    
    payer = x20*20 + x10*10 + x5*5 + x2*2 + x1
    rendu = payer - prix

    r20 = 0
    r10 = 0
    r5 = 0
    r2 = 0
    r1 = 0

    print('prix=', prix, ' payer=', payer, ' rendu=', rendu)
    if payer < prix:
        res = (None, None, None, None, None)
    elif payer == prix:
        res = (0, 0, 0, 0, 0)
    else:
        if rendu >= 20:
            r20 = rendu // 20
            rendu -= r20 * 20
        if rendu >= 10:
            r10 = rendu // 10
            rendu -= r10 * 10
        if rendu >= 5:
            r5 = rendu // 5
            rendu -= r5 * 5
        if rendu >= 2:
            r2 = rendu // 2
            rendu -= r2 * 2
        if rendu >= 1:
            r1 = rendu // 1

        res = (r20, r10, r5, r2, r1)
    return res

print(rendre_monnaie(80, 2, 2, 2, 3, 3))