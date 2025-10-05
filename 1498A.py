from math import gcd
for i in range(int(input())):
    n = int(input())

    x = n
    gcdsum = 1
    while gcdsum <= 1:
        b = list(str(x))
        s = sum([int(i) for i in b])
        gcdsum = gcd(x, s)
        x += 1

    print(x-1)