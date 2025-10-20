for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))

    if a <= c and b <= d:
        c -= a
        d -= b
        a,b = min(a,b), max(a,b)
        c,d = min(c,d), max(c,d)

        if b <= (a+1)*2 and d <= (c+1)*2:
            print('YES')
        else: print('NO')
    else:
        print('NO')