m,n = list(map(int, input().split()))
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

p = 2
while p * p <= n:
    if is_prime[p]:
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
    p += 1

primes = [i for i in range(n + 1) if is_prime[i]]

if primes[-1] == n and primes[-2] == m:
    print('YES')
else:
    print('NO')
