def my_insert(l,n):
    res = []
    placed = False

    if type(n) == int:
        for i in range(len(l)):
            if n < l[i] and placed == False:
                res.append(n)
                placed = True
            res.append(l[i])
    else:
        res = None
    
    return res

print(my_insert([1, 3, 5], 4))
print(my_insert([2, 3, 5], 1))
print(my_insert([2, 3, 5], 0.5))
