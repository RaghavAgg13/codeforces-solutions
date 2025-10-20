from collections import deque
from sys import stdin
input = stdin.readline

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ini_max = max(a[0], a[-1])
    if max(a) != ini_max:
        print(-1)
        continue 

    c = deque([ini_max])
    a.remove(ini_max)
    l,r = 0, n-2

    while l <= r:
        if a[l] <= a[r]: 
            c.appendleft(a[l])
            l += 1
        else:
            c.append(a[r])
            r -= 1
    
    print(*c)