def trace(M):
    c = 0
    for i in range(len(M)):
        c += M[i][i]

    return c


print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(trace([]))