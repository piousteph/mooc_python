def my_insert(l, n):
    assert(type(n) == int)

    for i in range(len(l)):
        if n < l[i]:
            l.insert(i, n)
            break

l = [1, 3, 5]
my_insert(l, 4)
print(l)