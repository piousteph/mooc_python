import math

def longueur(*points):

    dist = 0

    for p in range(len(points)-1):
        p1 = points[p]
        p2 = points[p+1]
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]

        dist += math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

    return dist

print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))
print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)))