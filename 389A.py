from math import gcd
n = int(input())
a = list(map(int, input().split()))

g = a[0]
for i in range(1, n):
    g = gcd(a[i], g)

print(g*n)