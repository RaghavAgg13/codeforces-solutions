from  math import gcd
for i in range(int(input())):
    n = int(input())
    m = gcd(n, 1) + 1
    idx = 1
    for i in range(1, n):
        a = gcd(n, i) + i
        if a > m:
            m = a
            idx = i

    print(idx)