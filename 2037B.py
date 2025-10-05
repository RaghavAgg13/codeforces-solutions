from sys import stdin
from math import isqrt
input = stdin.readline

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(list(a))

    left, right = 0, len(a)-1

    while left < right:
        area = a[left]*a[right]
        if area == n-2: 
            print(a[left], a[right])
            break
        elif area > n-2:
            right -= 1
        else: left += 1 