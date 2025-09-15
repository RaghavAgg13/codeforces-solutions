for i in range(int(input())):
    a,x,y = list(map(int, input().split()))
    x,y = min(x,y), max(x,y)

    if abs(a-x) +abs(a-y) > y-x:
        print('YES')
    else: print('NO')