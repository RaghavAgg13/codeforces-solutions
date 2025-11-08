def sieve(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

    return primes

def isPrime(n):
    for i in range(2, int(n//2)+1):
        if not n%i:
            return False
    
    return True            

n,k = list(map(int, input().split()))

b = sieve(n)[1:]
j = len(b)
a = 0
for i in range(j-1):
    # print(isPrime(b[i]+b[i+1]+1) and b[i]+b[i+1]+1 <= n)
    if isPrime(b[i]+b[i+1]+1) and b[i]+b[i+1]+1 <= n: a += 1

    if a >= k: break

# print(b,a)
print('YES' if a >= k else 'NO')