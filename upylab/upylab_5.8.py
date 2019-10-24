def anagrammes(v, w):
    res = True

    if (len(v) == len(w)):
        for iv in range(len(v)):
            iw = w.find(v[iv])
            if (iw == -1):
                res = False
                break
            w = w[:iw] + w[iw+1:]
    else:
        res = False

    return res

print(anagrammes('marion', 'romina'))
print(anagrammes('bonjour', 'jour'))
print(anagrammes('pate', 'patte'))
print(anagrammes('baignade', 'xadinage'))
