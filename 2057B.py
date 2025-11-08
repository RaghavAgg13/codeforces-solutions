import bisect
from collections import Counter
from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    b = sorted(Counter(input().split()).values())
 
    while k:
        delta = min(b[0], k)
        b[-1] += delta
        b[0] -= delta
        k -= delta
        
        if not b[0]: b.pop(0)
 
    print(len(b))
 

    # c = [0]
    # for i in b: c.append(c[-1]+i)
    # d = bisect.bisect_right(c, k)
    
    # print(len(c)-d if len(c)-d > 0 else 1)