for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))

    check = False
    for i in range(a,b+1):
        for j in range(c, d+1):
            if i != j:
                print(i, j)
                check = True
                break
        if check: break