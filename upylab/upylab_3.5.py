a = int(input())
b = int(input())

if (a / b) == (a // b) or (b / a) == (b // a):
    print(False)
else:
    print(True)