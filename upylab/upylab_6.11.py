def file_histogram(fileName):
    res = {}
    with open(fileName) as f:
        ls = f.readlines()
        for l in ls:
            for c in l:
                if c not in res:
                    res[c] = 0
                res[c] += 1
    return res

def vowels_histogram(fileName):
    v = 'aeiouyAEIOUY'
    res = {}
    tmp = ''
    with open(fileName) as f:
        ls = f.readlines()
        for l in ls:
            for c in l.strip():
                if c in v:
                    tmp += c
                elif tmp != '':
                    if tmp not in res:
                        res[tmp] = 0
                    res[tmp] += 1
                    tmp = ''
    return res

def words_by_length(fileName):
    s = ' \n\'\t,?!.-'
    res = {}
    tmp = ''
    with open(fileName) as f:
        ls = f.readlines()
        for l in ls:
            for c in l.strip().lower():
                if c not in s:
                    tmp += c
                elif tmp != '':
                    if len(tmp) not in res:
                        res[len(tmp)] = []
                    if tmp.lower() not in res[len(tmp)]:
                        res[len(tmp)].append(tmp.lower())
                        res[len(tmp)].sort()
                    tmp = ''
    return res


def c(t):
    for i in t:
        print(i, len(t[i]))

#print(file_histogram('Zola.txt'))
#print(vowels_histogram('Zola.txt'))
print(words_by_length('Zola.txt'))


c(words_by_length('Zola.txt'))
c({1: ['a', 'c', 'd', 'l', 'n', 's', 'à'], 2: ['ce', 'de', 'du', 'en', 'et', 'il', 'la', 'le', 'là', 'sa', 'se', 'si', 'un'], 3: ['aux', 'des', 'ils', 'les', 'par', 'pas', 'que', 'qui', 'ses', 'sol', 'une', 'vie'], 4: ['avec', 'blés', 'ciel', 'dans', 'dont', 'loin', 'plus', 'pour', 'sous', 'sève', 'tous', 'voix'], 5: ['armée', 'astre', 'avril', 'bruit', 'cette', 'comme', 'coups', 'faire', 'flanc', 'futur', 'grand', 'haies', 'noire', 'parts', 'pieds', 'pièce', 'plein', 'terre', 'vives', 'était'], 6: ['allait', 'arbres', 'autres', 'baiser', 'besoin', 'cassée', 'champs', 'chaque', 'droite', 'encore', 'gauche', 'germes', 'gloire', 'grosse', 'herbes', 'hommes', 'jeunes', 'plaine', 'rauque', 'rayons', 'rumeur', 'siècle', 'soleil', 'suivre', 'toutes', 'vertes', 'échine'], 7: ['bientôt', 'chaleur', 'coulait', 'croyait', 'fussent', 'germait', 'graines', 'lumière', 'maheude', 'matinée', 'montait', 'poussée', 'sillons', 'souffle', 'éclater', 'étaient'], 8: ['campagne', 'enjambée', 'feuilles', 'jeunesse', 'obstinés', 'profonds', 'récoltes', 'tapaient', 'épandait'], 9: ['bourgeons', 'camarades', 'crevaient', 'enfantait', 'enflammés', 'entendait', 'gerçaient', 'lentement', 'rayonnait'], 10: ['accompagné', 'betteraves', 'gonflaient', 'maintenant', 'nourricier', 'poussaient', 'rapprochés', 'rivelaines', 'ronflement', 'vengeresse', 'échauffant'], 11: ['débordement', 'germination', 'grandissant', 'jaillissait', 'reconnaître', 'travaillées', 'ventilateur'], 12: ['allongeaient', 'chuchotantes', 'continuaient'], 13: ['distinctement'], 14: ['tressaillaient']})