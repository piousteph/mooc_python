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

def liste_des_mots(in_path):

    res = []
    tmp = []

    with open(in_path, encoding="utf-8") as fin:
        for l in fin:
            tmp += mysplit(l.strip(), " \"-'?!:;.,*=()1234567890\t")
    
    tmp.sort()

    for i in range(len(tmp)):
        if res.count(tmp[i]) == 0:
            res.append(tmp[i])

    return res

print(liste_des_mots('le-petit-prince.txt'))