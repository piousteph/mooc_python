def top_3_candidats(moyennes):
    res = ()
    tmp = []

    for c in moyennes:
        tmp.append(moyennes[c])

    tmp.sort(reverse=True)

    for i in range(3):
        for c in moyennes:
            if tmp[i] == moyennes[c]:
                res += (c,)
                break
    return res

print(top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33}))