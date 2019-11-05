def even(lst):
    res = set()

    for n in range(len(lst)):
        if lst[n] % 2 != 0:
            res.add(lst[n])

    return res


def prime_numbers(lst):
    res = set()

    for n in range(len(lst)):
        p = True
        i = lst[n]
        if i < 2:
            p = False
        for x in range(2, i):
            if (i % x) == 0:
                p = False
        if p == True:
            res.add(i)

    return res



def prime_odd_numbers(numbers):
    return (prime_numbers(numbers), even(numbers))

print(prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18]))
# (set(), {1, 9, 15, 21})

print(prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18]))
# ({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17})