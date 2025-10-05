for i in range(int(input())):
    a = list(input())

    b = len(set(a))

    if b >= 3: print(4)
    elif b == 2:
        if a.count(a[0]) == 1 or a.count(a[0]) == 3:
            print(6)
        else: print(4)
    else:
        print(-1)