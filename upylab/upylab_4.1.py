def deux_egaux(a, b, c):
    return a == b or a == c or b == c


a = int(input())
b = int(input())
c = int(input())
print(deux_egaux(a, b, c))