def mysplit(s, delimiters):
    res = []
    tmp = ''
    for i in range(len(s)):
        if delimiters.find(s[i]) != -1:
            if tmp != '':
                res.append(tmp.lower())
                tmp = ''
        else:
            tmp += s[i]

    if tmp != '':
        res.append(tmp.lower())
    
    return res


def wc(nomFichier):
    fulllength = 0
    wcount = 0
    lcount = 0

    with open(nomFichier, encoding="utf-8") as file:
        lcount = len(file.readlines())
        file.seek(0)
        fullcontent = file.read()

        fulllength = len(fullcontent)
        wcount = len(mysplit(fullcontent, " \"-'?!:;.,*=()\t\n"))

    return (fulllength, wcount, lcount)

print(wc("wc1.txt"))
print(wc("le-petit-prince.txt"))
print(wc("Zola.txt"))
