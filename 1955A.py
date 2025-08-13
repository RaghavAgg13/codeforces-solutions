for i in range(int(input())):
    n, a, b = list(map(int, input().split()))

    if a*2 > b:
        if n >= 2:
            cost = b*(n//2) + a*(n%2)
        else: cost = a*n
    else: cost = a*n

    print(cost)