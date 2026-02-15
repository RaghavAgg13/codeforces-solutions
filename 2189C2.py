from math import log2
import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())

    if (2**(int(log2(n))) == n):
        print(-1)
        continue

    a = [0]*(n+1)
    check = [False]*(n+1)

    a[n] = 1
    check[1] = True
    for i in range(2, n):
        a[i] = i^1
        check[i^1] = True

    for i in range(1, n+1):
        if (not check[i]):
            a[1] = i
            break

    if (not n%2):
        a[n&(-n)], a[1] = a[1], a[n&(-n)]

    print(*a[1:])