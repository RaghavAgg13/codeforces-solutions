for i in range(int(input())):
    x,y,k = list(map(int, input().split()))

    while (k > 0 and x > 1):
        change = min(k, (y - x%y))
        x += change
        k -= change


        while (not x%y):
            x //= y
    
    if (x == 1 and k > 0):
        x = 1+k%(y-1)

    print(x)