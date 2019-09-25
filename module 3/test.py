x = 10
print("not (0 <= x and x < 10)", not (0 <= x and x < 10))
print("0 <= x or x < 10", 0 <= x or x < 10)
print("not (0 <= x and x < 10)", not (0 <= x and x < 10))
print("DE MORGAN: not (0 <= x) and not (x < 10)", not (0 <= x) and not (x < 10))

for x in range(5):
    for y in range(4):
        print(x, y)