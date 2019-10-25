def distance_mots(mot_1, mot_2):
    res = 0
    for i in range(len(mot_1)):
        if mot_1[i] != mot_2[i]:
            res += 1
    return res

def correcteur(mot, liste_mots):
    res = mot
    min_diff = 100

    for i, a in enumerate(liste_mots):
        if len(a) == len(mot):
            diff = distance_mots(mot, a)
            if diff < min_diff:
                res = a
                min_diff = diff
    return res

print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
