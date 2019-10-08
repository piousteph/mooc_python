import math

def distance_points(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

print(distance_points((1.0, 1.0), (2.0, 1.0)))
print(distance_points((-1.5, 3.0), (-1.0, 3.0)))
print(distance_points((-1.0, 0.5), (2.0, 1.0)))