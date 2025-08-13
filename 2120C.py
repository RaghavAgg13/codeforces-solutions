MOD = 10**9 + 7

for i in range(int(input())):
    a, b, k = map(int, input().split())
    n1, m1 = a * k, b
    n2, m2 = a, b * k
    if n1 < n2 or (n1 == n2 and m1 < m2):
        print(n1 % MOD, m1 % MOD)
    else:
        print(n2 % MOD, m2 % MOD)
