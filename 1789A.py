from math import gcd
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if gcd(a[i], a[j]) <= 2:
                check = 1
                break
        if check: break

    if check:
        print('YES')
    else:
        print('NO')