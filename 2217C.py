from math import gcd
for i in range(int(input())):
    n,m,a,b = list(map(int, input().split()))

    if gcd(n, a) == 1 and gcd(m, b) == 1 and gcd(n, m) <= 2:
        print("YES")
    else:
        print("NO")