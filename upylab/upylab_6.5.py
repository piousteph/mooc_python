def symetrise_amis(d, englobe):

    for i in d:
        di = d[i].copy()

        for j in d[i]:
            if englobe == True:
                d[j].add(i)
            elif i not in d[j]:
                di.remove(j)
        d[i] = di.copy()


d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, True)
print(d)

# {'Thierry': {'Michelle', 'Bernadette'},
#  'Michelle' : {'Thierry'},
#  'Bernadette' : {'Thierry'}}


d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, False)
print(d)

# {'Thierry': {'Michelle'},
#  'Michelle' : {'Thierry'},
#  'Bernadette' : set()}