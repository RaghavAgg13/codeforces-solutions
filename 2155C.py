for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    zerocheck = 1
    for i in range(1, n):
        if a[i]-a[i-1] != 0: 
            zerocheck = 0
            break

    if zerocheck: print(2)
    else:
        for 