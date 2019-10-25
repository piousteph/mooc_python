def my_remove(lst, e):
    if type(lst) == list and lst.count(e) > 0:
        lst.remove(e)

l = [1, 2, 3, 4, 3, 2, 1]
my_remove(l, 2)
print(l)

l = (1, 2, 3)
my_remove(l, 2)
print(l)

l = [1, 5, 78]
my_remove(l, 'p')
print(l)