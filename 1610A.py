for i in range(int(input())):
    n,m = list(map(int, input().split()))

    if n == m == 1: print(0)
    elif n == 1 or m == 1: print(1)
    else: print(2)