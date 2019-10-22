def plus_grand_bord(w):
    res = ''
    for i in range(1, len(w) - 1):
        if (w[:i] == w[len(w)-i:]):
            res = w[:i]
    return res

print(plus_grand_bord('abdabda'))
print(plus_grand_bord('abcabd'))
print(plus_grand_bord('abcba'))
