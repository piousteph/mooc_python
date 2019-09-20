#coding:utf-8

import random

class Fourmie:

  def __init__(self, pere, mere, sexe):
    global nbDeces
    self.id = len(fourmies)
    if pere == 0:
      self.pere = 0
    else:
      self.pere = pere.id
      pere.nbEnfant = pere.nbEnfant + 1
    
    if mere == 0:
      self.mere = 0
    else:
      self.mere = mere.id
      mere.nbEnfant = mere.nbEnfant + 1
      
    self.sexe = sexe
    self.nbEnfant = 0
    self.tentative = 0
    print("Naissance de {}, de pere {} et de mere {} et de sexe {}".format(len(fourmies), self.pere, self.mere, sexe))

    if pere != 0 and pere.nbEnfant > 2:
      nbDeces = nbDeces + 1
      fourmies.remove(pere)
      print("Trop de responsabilite, le pere est mort")

    if mere != 0 and mere.nbEnfant > 2:
      nbDeces = nbDeces + 1
      fourmies.remove(mere)
      print("Trop de grossesse, la mere est morte")


def tentatives(fourmie):
  global nbDeces
  fourmie.tentative = fourmie.tentative + 1
  if fourmie.tentative > 5:
    print("Fourmie {} a essaye trop de fois et est morte".format(fourmie.id))
    nbDeces = nbDeces + 1
    fourmies.remove(fourmie)

nbNaissance = 0
nbDeces = 0
fourmies = list()

fourmies.append(Fourmie(0,0,0))
fourmies.append(Fourmie(0,0,0))
fourmies.append(Fourmie(0,0,1))
fourmies.append(Fourmie(0,0,1))

while len(fourmies) < 10000:

  if len(fourmies) < 2:
    print("La colonie est morte :(")
    break
  # tire au sort 2 id de fourmies
  nf1 = random.randint(0, len(fourmies)-1)
  nf2 = random.randint(0, len(fourmies)-1)

  #recommence si les 2 id sont identiques
  while nf2 == nf1:
    nf2 = random.randint(0, len(fourmies)-1)

  # recupere les fourmies
  f1 = fourmies[nf1]
  f2 = fourmies[nf2]

  # verifie si compatible
  # pas du meme sexe
  # pas de frere et soeur
  if f1.sexe == f2.sexe:
    tentatives(f1)
    tentatives(f2)
    # print("Meme sexe")
    continue

  if f1.pere == f2.pere and f1.pere != 0 and f2.pere != 0:
    tentatives(f1)
    tentatives(f2)
    # print("Meme Pere")
    continue
    
  if f1.mere == f2.mere and f1.mere != 0 and f2.mere != 0:
    tentatives(f1)
    tentatives(f2)
    # print("Meme Mere")
    continue

  if f1.sexe == 0:
    pere = f1
    mere = f2
  else:
    pere = f2
    mere = f1

  fourmies.append(Fourmie(pere, mere, random.randint(0, 1)))
  print("Nombre de fourmies => {}".format(len(fourmies)))
  nbNaissance = nbNaissance + 1

print("Nombre de naissance {}".format(nbNaissance))
print("Nombre de deces {}".format(nbDeces))

