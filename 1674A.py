for i in range(int(input())):
    x,y = list(map(int, input().split()))

    if x > y: print("0 0")
    elif x == y: print("1 1")
    else:
        if y%x:
            print("0 0")
        else:
            d = y//x
            print(1, d)