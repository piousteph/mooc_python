def next_line(line):
    res = []
    prev = 0
    nb = 0
    for i in range(len(line)):
        if prev == 0:
            prev = line[i]
            nb = 1
        else:
            if prev == line[i]:
                nb += 1
            else:
                res.append(nb)
                res.append(prev)
                prev = line[i]
                nb = 1

    if nb != 0:
        res.append(nb)
        res.append(prev)
    else:
        res.append(1)

    return res



print(next_line([1, 2, 1, 1]))
print(next_line([1]))
print(next_line([]))