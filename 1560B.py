for i in range(int(input())):
    a,b,c = list(map(int, input().split()))
    a,b = max(a,b), min(a,b)

    n = (a-b)*2
    if n%2==1:
        print(-1)
    else:
        if a > n or b > n or c > n:
            print(-1)
        elif n >= c:
            d = max(c-n//2, c+n//2)
            if d > n: d = c-n//2
            print(d)
        else:
            print(-1)