for _ in range(int(input())):
    n,x,m = list(map(int, input().split()))

    upper = x
    lower = x

    cnt = 1
    for i in range(m):
        a,b = sorted(list(map(int, input().split())))

        if max(upper, a) <= min(lower, b):
            upper = min(upper, a)
            lower = max(lower, b)
            cnt = lower-upper+1
        
    print(cnt)