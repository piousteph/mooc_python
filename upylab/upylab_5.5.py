def trans(text, replaceA, replaceB):
    res = ''
    for i in range(len(text)):
        if (text[i] == replaceA[0]):
            res += replaceA[1]
        elif (text[i] == replaceB[0]):
            res += replaceB[1]
        else:
            res += text[i]
    return res

print(trans('ABBAB', ('A','AB'), ('B','BA')))
print(trans('piton', ('i','y'), ('t','th')))