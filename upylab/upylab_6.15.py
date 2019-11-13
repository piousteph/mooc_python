def readdata(filename):
    res = []
    tmp = []
    with open(filename) as f:
        l = f.readlines()
        for i in range(len(l)):
            tmp.append(l[i].strip().split(';'))
    
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if j > len(res)-1:
                res.append([])
            res[j].append(tmp[i][j])
    return res

def getfiable(c):
    res = []

def getexvalue(n, pf, c):
    res = []
    for i in range(1, len(pf[n])):
        if pf[n][i] == 'VRAI' and c[n][i] < 10







pf = input()
c = input()

pf = 'result-pass-fail-0.csv'
c = 'result-count-0.csv'

datapf = readdata(pf)
datac = readdata(c)

print(datapf)
getexvalue(1,datapf, datac)

