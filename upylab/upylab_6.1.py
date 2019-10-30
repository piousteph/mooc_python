def calcul_prix(produits, catalogue):
    res = 0
    for p in produits:
        res += produits[p] * catalogue[p]
        
    return res




print(calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
            {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
             "savon":2.50, "mouchoirs":0.80}))