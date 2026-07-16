from math import gcd
n = int(input())

cnt = 0
for i in range(n//2, 0, -1):
    if gcd(i, n-i) == 1:
        print(i, n-i)
        break