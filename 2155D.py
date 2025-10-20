for i in range(int(input())):
    n = int(input())

    check = 0
    for gap in range(1, n):
        for i in range(1, n+1-gap):
            print(i, i+gap, flush=True)
            check = int(input())

            if check: break
        if check: break