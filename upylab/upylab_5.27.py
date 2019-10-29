def symetrie_horizontale(A):
    res = []
    for i in range(len(A)-1 , -1, -1):
        res.append(A[i])

    return res


print(symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(symetrie_horizontale([['a', 'b'], ['c', 'd']]))
print(symetrie_horizontale([]))