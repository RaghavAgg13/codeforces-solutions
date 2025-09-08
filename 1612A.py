for i in range(int(input())):
    x,y = list(map(int, input().split()))

    if not x%2 and not y %2:
        print(x//2, y//2)
    elif x%2 and y%2:
        if x >= y: print((x-y)//2,y)
        else: print(x, (y-x)//2)
    else:
        print("-1 -1")