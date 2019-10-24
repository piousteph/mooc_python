def prime_numbers(nb):
    res = []
    num = 2
    if type(nb) == int and nb >= 0:
        while len(res) != nb:
            prem = True
            for i in range(num - 1, 1, -1):
                if num % i == 0:
                    prem = False
                    break
            if prem:
                res.append(num)
            num += 1
    else:
        res = None

    return res

print(prime_numbers(4))
print(prime_numbers(0))
print(prime_numbers(-2))
