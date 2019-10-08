
def duree(debut, fin):
    d = debut[0] * 60 + debut[1]
    f = fin[0] * 60 + fin[1]

    e = f - d

    h = e // 60
    m = e - h * 60
    if h < 0:
        h = 24 - abs(h)
    return (h, m)

print(duree ((14, 39), (18, 45)))
print(duree ((6, 0), (5, 15)))