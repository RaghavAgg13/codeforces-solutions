for i in range(int(input())):
    a,b,c,x,y = list(map(int, input().split()))

    rem = 0
    if a < x:
        rem += x-a
    
    if b < y:
        rem += y-b

    if c >= rem:
        print('YES')
    else:
        print('NO')