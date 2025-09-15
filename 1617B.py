from math import gcd
for i in range(int(input())):
    n = int(input())

    c = 1
    a,b = 1,1
    for i in range(2, n):
        if gcd(i, n-1-i) == 1 and n-1-i != 1:
            a,b = i, n-1-i
            break

    print(a,b,c)