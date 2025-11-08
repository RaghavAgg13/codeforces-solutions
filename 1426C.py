from math import ceil
for i in range(int(input())):
    n = int(input())

    ans = n
    mid = ceil(n**0.5)
    for i in [mid, mid+1]:
        ans = min(ans, i-1+ceil(n/i))
    
    print(ans-1)