from sys import stdin
input = stdin.readline

MOD = 1000000007
MAX_F = 200005

fact = [1]*MAX_F
inv = [1]*MAX_F
for i in range(1, MAX_F):
    fact[i] = (fact[i-1]*i)%MOD

inv[MAX_F-1] = pow(fact[MAX_F-1], MOD-2, MOD)
for i in range(MAX_F-2, -1, -1):
    inv[i] = (inv[i+1]*(i+1))%MOD

def nCr(n,r):
    if r < 0 or r > n: return 0
    return fact[n] * inv[r]%MOD * inv[n-r]%MOD

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
    max_ai = max(max_ai, x)

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

    cprimes = {}
    while x > 1:
        if spf[x] not in cprimes: cprimes[spf[x]] = 1
        else: cprimes[spf[x]] += 1

        x //= spf[x]

    primes = set()
    divisors = [set() for _ in range(n)]

    for j in range(n):
        x = a[j]

        while spf[x] > 1:
            primes.add(spf[x])
            divisors[j].add(spf[x])
            x //= spf[x]
    
    d = {}
    for x in primes:
        d[x] = {}
    
    for j in range(n):
        for x in divisors[j]:
            freq = 0

            while a[j]%x == 0:
                a[j] //= x
                freq += 1

            if not freq: continue

            if (freq not in d[x]): d[x][freq] = 1
            else: d[x][freq] += 1
    
    prod = 1
    
    all_primes = primes.union(cprimes.keys())
    
    for p in all_primes:
        if p not in cprimes:
            no = 1
            for key, val in d[p].items():
                no = (no+key*val)%MOD
            prod = (prod*no)%MOD
            
        else:
            if p not in d:
                prod = 0
                break

            X_pow = cprimes[p]
            max_m = max(d[p].keys()) if d[p] else 0
            
            # Total voters who have at least one power of p
            k = sum(val for key, val in d[p].items() if key >= 1)
            if k == 0:
                prod = 0
                break
                
            def W(M, S):
                if M <= 0: return 0
                
                # poly[i] stores the coefficient of y^i
                poly = [0]*(S+1)
                poly[0] = 1
                
                for L in range(1, M+1):
                    # C_L is the number of voters bounded by exactly L
                    if L < M:
                        C_L = d[p].get(L, 0)
                    else:
                        C_L = sum(v for k_m,v in d[p].items() if k_m >= M)
                        
                    if C_L == 0: continue
                    
                    # Multiply poly by (1 - y^(L+1))^C_L
                    new_poly = [0] * (S + 1)
                    for i in range(S + 1):
                        if poly[i] == 0: continue
                        for j in range(C_L+1):
                            deg = i+j*(L+1)
                            if deg > S: break
                            
                            term = (nCr(C_L, j) * poly[i]) % MOD
                            if j % 2 == 1: # Subtraction for odd j
                                new_poly[deg] = (new_poly[deg] - term + MOD)%MOD
                            else:          # Addition for even j
                                new_poly[deg] = (new_poly[deg] + term)%MOD
                    poly = new_poly
                    
                # Multiply by (1 - y)^(-k) which is sum(nCr(k+j-1, j) * y^j)
                ans = 0
                for i in range(S+1):
                    j = S-i
                    ans = (ans + poly[i]*nCr(k+j-1, j))%MOD
                return ans

            ways_p = 0
            for M in range(1, max_m + 1):
                S = X_pow + M
                ways_p = (ways_p+W(M, S)-W(M-1, S)+MOD)%MOD
                
            prod = (prod*ways_p)%MOD

    print(prod)