from sys import stdin
import math

input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    fr = sorted(set(map(int, input().split())))
    b = list(map(int, input().split()))
    
    max_b = max(b)
    
    # get lcm of all elements
    L = 1
    for x in fr:
        L = (L*x)//math.gcd(L, x)
        
        if L > max_b: break
            
    a = 0
    if L <= max_b:
        for y in b:
            if y % L == 0:
                a += 1
                
    # 2. Use a Sieve to find # at least div by one a
    freq = {}
    for y in b:
        freq[y] = freq.get(y, 0) + 1
        
    d = 0
    marked = [False]*(max_b+1)
    for x in fr:
        if x > max_b:
            break

        if not marked[x]:
            for multiple in range(x, max_b + 1, x):
                if not marked[multiple]:
                    marked[multiple] = True
                    if multiple in freq:
                        d += freq[multiple]
                        
    bob_only = m-d
    shared = d-a

    if shared%2 == 1:
        if a >= bob_only:
            print("Alice")
        else:
            print("Bob")
    else:
        if a > bob_only:
            print("Alice")
        else:
            print("Bob")