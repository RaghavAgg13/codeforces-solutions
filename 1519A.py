for i in range(int(input())):
    r,b,d = list(map(int, input().split()))

    if d == 0:
        print('YES' if r == b else 'NO')
    else: 
        if abs(r-b) <= d*min(r,b): print('YES')
        else: print('NO')