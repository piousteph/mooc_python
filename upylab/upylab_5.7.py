def my_pow(m, b):
    res = []
    if type(m) is int and type(b) is float:
        for i in range(m):
            res.append(b**i)
    else:
        res = None
    return res

print(my_pow(3, 5.0))
print(my_pow(3.0, 5.0))
print(my_pow('a', 'b'))
