def catalan(n):
    res = 1

    for n in range(0, n):
        res = (4*n+2) / (n+2) * res
    return int(res)



print(catalan(int(input())))