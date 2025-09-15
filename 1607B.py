for i in range(int(input())):
    x,n = list(map(int, input().split()))

    rem = n%4

    if not rem: print(x)
    elif rem == 1:
        print(x+n if x%2 else x-n)
    elif rem == 2:
        print(x-1 if x%2 else x+1)
    else:
        print(x-n-1 if x%2 else x+n+1) 