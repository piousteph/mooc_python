def intersection(v, w):
    res = ''
    tmpres = ''

    for i in range(len(v)):
        tmpres += v[i]
        print('cherche', tmpres, 'dans', w, 'done', w.find(tmpres))
        if w.find(tmpres) == -1:
            tmpres = tmpres[:-1]
            if len(tmpres) > len(res):
                res = tmpres
                tmpres = ''
    
    return res


print(intersection('programme', 'grammaire'))
print(intersection('salut', 'merci'))
print(intersection('merci', 'adieu'))
print(intersection('bbaacc', 'aabb'))
