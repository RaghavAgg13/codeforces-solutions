for i in range(int(input())):
    b,p,f = list(map(int, input().split()))
    h,c = list(map(int, input().split()))

    profit = 0
    if c >= h:
        if b > f*2:
            profit += c*f
            b -= f*2

            if b > p*2: profit += h*p
            else: profit += h*(b//2)
        else:
            profit += c*(b//2)
    else:
        if b > p*2:
            profit += h*p
            b -= p*2

            if b > f*2: profit += c*f
            else: profit += c*(b//2)

        else:
            profit += h*(b//2)

    print(profit)