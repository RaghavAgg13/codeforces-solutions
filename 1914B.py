for i in range(int(input())):
    n,k = list(map(int, input().split()))

    if k == n-1:
        print(*[i for i in range(1, n+1)])
    elif k == 0:
        print(*[i for i in range(n, 0, -1)])
    else:
        print(*[1], *[i for i in range(n-k+1, n+1)], *[i for i in range(n-k, 1, -1)])