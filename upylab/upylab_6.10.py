def compteur_lettres(texte):
    res = {}
    for i in range(97,123):
        res[chr(i)] = 0

    for i in texte.lower():
        if i in res:
            res[i] += 1
    return res

print(compteur_lettres("Dessine-moi un mouton !"))

# {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2,
# 'f': 0, 'g': 0, 'h': 0, 'i': 2, 'j': 0,
# 'k': 0, 'l': 0, 'm': 2, 'n': 3, 'o': 3,
# 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1,
# 'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
# 'z': 0}

print(compteur_lettres('Je viens d’arriver a l’Universite Libre de Bruxelles et pour l’instant je m’y plais tres bien.'))
# {'o': 1, 'n': 5, 'v': 3, 'r': 8, 'm': 1, 'd': 2, 'b': 3, 'u': 3, 'k': 0, 'g': 0, 'q': 0, 'h': 0, 'e': 13, 'z': 0, 'a': 4, 'x': 1, 'c': 0, 'f': 0, 'p': 2, 't': 5, 'i': 8, 'w': 0, 'j': 2, 's': 6, 'l': 6, 'y': 1}
# {'a': 4, 'b': 2, 'c': 0, 'd': 2, 'e': 13, 'f': 0, 'g': 0, 'h': 0, 'i': 8, 'j': 1, 'k': 0, 'l': 5, 'm': 1, 'n': 5, 'o': 1, 'p': 2, 'q': 0, 'r': 8, 's': 6, 't': 5, 'u': 2, 'v': 3, 'w': 0, 'x': 1, 'y': 1, 'z': 0}