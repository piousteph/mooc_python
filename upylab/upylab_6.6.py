def valeurs(dico):
    res = []
    tmp = []

    for k in dico:
        tmp.append(k)

    tmp.sort()
    
    for k in tmp:
        res.append(dico[k])

    return res


print(valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}))