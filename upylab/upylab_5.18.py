def my_filter(lst, l):
    return [lst[i] for i in range(len(lst)) if l(lst[i])]

print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0))