def distance_mots(mot_1, mot_2):
    res = 0
    for i in range(len(mot_1)):
        if mot_1[i] != mot_2[i]:
            res += 1
    return res

print(distance_mots("lire", "bise"))
print(distance_mots("Python", "Python"))
print(distance_mots("merci", "adieu"))
