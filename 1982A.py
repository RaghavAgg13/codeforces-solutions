for i in range(int(input())):
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))


    if (x1-y1)*(x2-y2) >= 0: print('YES')
    else: print('NO')