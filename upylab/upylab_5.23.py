def init_mat(m, n):
    res = []

    for i in range(0, m):
        res.append([])
        for j in range(0, n):
            res[i].append([])
            res[i][j] = 0
    return res

print(init_mat(2, 3))
print(init_mat(0, 0))