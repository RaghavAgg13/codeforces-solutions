from sys import stdin
input = stdin.readline

n_, x_ = [], []
a_ = []
max_ai = 0

t = int(input())
for i in range(t):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    n_.append(n)
    x_.append(x)
    a_.append(a)

    max_ai = max(max_ai, max(a))

def get_spf(lim):
    spf = [0 for _ in range(lim+1)]
    spf[1] = 1

    for i in range(2, lim+1):
        if spf[i] == 0:
            spf[i] = i

            for j in range(i*2, lim+1, i):
                spf[j] = i

    return spf
spf = get_spf(max_ai)

for i in range(t):
    n,x = n_[i], x_[i]
    a = a_[i]

    primes = set()
    divisors = [set() for _ in range(n)]

    for i in range(n):
        x = a[i]

        while spf[x] > 1:
            primes.add(spf[x])
            divisors[i].add(spf[x])
            x //= spf[x]
    
    d = {}
    for x in primes:
        d[x] = {}
    
    for i in range(n):
        for x in divisors[i]:
            freq = 0

            while a[i]%x == 0:
                a[i] //= x
                freq += 1

            if not freq: continue

            if freq not in d[x]: d[x][freq] = 1
            else: d[x][freq] += 1
    
    prod = 1
    for x in primes:
        no = 1
        for key,val in d[x].items(): no += key*val
        prod = (prod*no)%1000000007

    print(prod)