from math import pi, sin, cos

long = float(input())
print(long * cos(0), long * sin(0))
print(long * cos(pi / 3), long * sin(pi / 3))
print(long * cos(pi * 2 / 3), long * sin(pi * 2 / 3))
print(-long, 0.0)
print(long * cos(4 / 3 * pi), long * sin(4 / 3 * pi))
print(long * cos(5 / 3 * pi), long * sin(5 / 3 * pi))