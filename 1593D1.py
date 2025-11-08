from math import gcd
from sys import stdin
input = stdin.readline

for j in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    min_val = min(a)
    if all(x == min_val for x in a):
        print(-1)
        continue

    diff = 0
    for i in a:
        diff = gcd(diff, i-min_val)

    print(diff)