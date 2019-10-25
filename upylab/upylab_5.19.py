val = ""
entrees = []
while val != "FINI":
    val = input()
    entrees.append(val)

with open(entrees[0]) as story:
    s = story.read()

for i, e in enumerate(entrees[1:len(entrees)-1]):
    s = s.replace('{' + str(i) + '}', e)

print(s.strip())
