from math import ceil 
n,m = list(map(int, input().split()))

count = 0
for a in range(ceil(n**0.5)+1):
    for b in range(ceil(m**0.5)+1):
        if a**2 + b == n and a + b**2==m:
            count += 1

print(count)