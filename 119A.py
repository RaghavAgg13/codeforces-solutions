from math import gcd
a,b,n = list(map(int, input().split()))
check = True

while True:
    n -= gcd(a,n)
    if not n: break
    n -= gcd(b,n)
    if not n:
        check = False
        break

print(0 if check else 1)