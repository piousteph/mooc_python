def my_count(lst, e):
    res = 0
    if type(lst) == list:
        res = lst.count(e)
    return res

print(my_count([1, 2, 3, 4, 3, 2, 1], 3))
print(my_count([1, 2, 3], 4))
print(my_count((2, 3, 5), 3))