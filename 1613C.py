def crit(k, arr):
    return sum([min(i, k) for i in arr])+k

from math import ceil
for i in range(int(input())):
    n,h = list(map(int, input().split()))
    a = list(map(int, input().split()))

    diff = [a[i]-a[i-1] for i in range(1, n)]

    left = 1
    right = h
    ans = 10000000000
    while (left <= right):
        mid = left + (right-left)//2
        damage = crit(mid, diff)
        if damage == h: 
            ans = mid
            break
        elif damage > h :
            ans = mid
            right = mid-1
        else:
            left = mid+1
    
    if ans == 10000000000: ans = left
    
    print(ans)