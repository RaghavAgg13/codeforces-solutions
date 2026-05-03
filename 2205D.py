for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    L = [0 for _ in range(n)]
    left_greater = [0 for _ in range(n)]
    top = 0
    for i in range(n):
        while top > 0 and a[L[top-1]] < a[i]: top -= 1
        
        if top > 0: left_greater[i] = L[top-1]
        else: left_greater[i] = -1

        L[top] = i
        top += 1
    
    L = [0 for _ in range(n)]
    right_greater = [0 for _ in range(n)]
    top = 0
    for i in range(n-1, -1, -1):
        while top > 0 and a[L[top-1]] < a[i]: top -= 1
        
        if top > 0: right_greater[i] = L[top-1]
        else: right_greater[i] = -1

        L[top] = i
        top += 1

    pos = [0]*(n+1)
    for i in range(n): pos[a[i]] = i

    d = [1] * n
    for v in range(n, 0, -1):
        i = pos[v]
        l, r = left_greater[i], right_greater[i]
        p = r if l == -1 else l if r == -1 else l if a[l] < a[r] else r
        if p != -1: d[i] = d[p] + 1

    print(n - max(d))