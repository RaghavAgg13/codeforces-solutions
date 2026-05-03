from sys import stdin
from math import log2, floor
input = stdin.readline

for i in range(int(input())):
    s,m = list(map(int, input().split()))

    b = m

    max_power = 2**(floor(log2(m)))
    twos = set()
    while m > 0:
        cnt = m//max_power
        if (cnt > 0): twos.add(max_power)
        m -= cnt*max_power
        
        max_power //= 2

    twos = sorted(list(twos), reverse=True)

    if s%twos[-1]:
        print(-1)
        continue

    l = max(1, s//b)
    r = s//twos[-1]
    ans = -1

    while l <= r:
        mid = (l+r)//2

        rem = s
        for bit in twos:
            take = min(mid, rem//bit)
            rem -= take*bit

        if rem == 0:
            ans = mid
            r = mid-1
        else:
            l = mid+1

    print(ans)