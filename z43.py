def prime(x):
    for i in range(2,x):
        if x%i == 0:
            return 0
    return 1

def tprime(x):
    y = int(x)
    z = int(x[::-1])
    if prime(y):
        if prime(z):
            return 1
        else:
            return 0
    else:
        return 0

with open('liczby.txt', 'r') as plik:
    pr = []
    for l in plik:
        l = l.strip()
        if tprime(l):
            pr.append(int(l))

for el in pr:
    print(el)

# 157
# 31
# 347
# 929
# 941
# 761