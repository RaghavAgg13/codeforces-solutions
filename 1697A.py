for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    s = 0
    check = 1

    # for i in range(n):
    #     s += a[i]
    #     if check and a[i] != i:
    #         check = 0
    
    # if check: print(0)

    s = sum(a)
    print(max(s-m, 0))
