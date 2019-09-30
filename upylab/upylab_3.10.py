i = 0
total = 0
nbentree = 0

while i != -1:
    i = int(input())
    if i != -1:
        total += i
        nbentree += 1

print(total/nbentree)