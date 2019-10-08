import math

def rac_eq_2nd_deg(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    res = tuple()

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        res = (min(x1, x2), max(x1, x2))
    elif delta == 0:
        x1 = -b / (2 * a)
        res = (x1,)
    return res

print(rac_eq_2nd_deg(1.0,-4.0,4.0))