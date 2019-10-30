def construction_dict_amis(couples):
    res = {}

    for i in couples:
        if i[0] not in res:
            res[i[0]] = set()
        if i[1] not in res:
            res[i[1]] = set()
        res[i[0]].add(i[1])

    return res


print(construction_dict_amis([('Quidam', 'Pierre'), ('Thierry', 'Michelle'), ('Thierry', 'Pierre')]))
# {'Quidam' : {'Pierre'}, 'Pierre' : set(), 'Thierry' : {'Michelle', 'Pierre'}, 'Michelle' : set()}