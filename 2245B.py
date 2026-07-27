for _ in range(int(input())):
    n,c = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = [a[i]-c for i in range(n)]

    cnt = sum([1 for i in b if i > 0])
    
    b.sort()

    l, r = cnt, n-cnt-1
    s = sum(b[n-cnt:])

    while l <= r:
        s += b[r]
        l += 1
        r -= 1
    
    print(s)