def fibo(n):
    A=0
    B=1
    if n < 0:
        return None
    if n == 0: 
        return 0
    if n == 1:
        return 1
     
    for i in range(2, n + 1):
        C=A+B
        A=B
        B=C
    return B

x = int(input())
for i in range(0, x):
    print(fibo(i))

print('alone', fibo(x))