for i in range(int(input())):
    a,b = list(map(int, input().split()))

    if b-abs(a) > -1*abs(a)-2: print('YES')
    else: print('NO')