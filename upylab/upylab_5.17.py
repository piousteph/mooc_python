def decompresse(lst):
    return [lst[i][1] for i in range(len(lst)) for j in range(lst[i][0])]

print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))
