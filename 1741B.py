for i in range(int(input())):
    n = int(input())

    if n == 3:
        print(-1)
    elif not n%2:
        for i in range(n, 0, -1): print(i, end=' ')
        print()
    else:
        print(n, n-1, end=' ')
        for i in range(1, n-1): print(i, end=' ')
        print()
