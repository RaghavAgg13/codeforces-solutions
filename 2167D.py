from sys import stdin
from math import gcd
input = stdin.readline

for i in range(int(input())):
    n = int(input())
    a = set(map(int, input().split()))

    x = 10**18
    for j in range(2, 101):
        for i in a:
            if gcd(i, j) == 1: 
                x = j
                break
        if x != 10**18: break

    print(x)