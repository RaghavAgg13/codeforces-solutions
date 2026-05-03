for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = int(input())-1

    l,r = 0,0

    for i in range(p, 0, -1):
        if a[i] != a[i-1]: l += 1
    for i in range(p, n-1):
        if a[i] != a[i+1]: r += 1
    
    l += (a[0] != a[p])
    r += (a[-1] != a[p])

    print(max(l, r))