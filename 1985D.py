for i in range(int(input())):
    n,m = list(map(int, input().split()))
    
    b = True
    starth = 0
    endh = 0
    maxcount = 0
    xcord = 0
    for i in range(n):
        a = input()

        if a.count('#') > maxcount:
            maxcount = a.count("#")
            xcord = a.index('#')+1+maxcount//2

        if '#' in a:
            endh = i+1
            if b:
                starth = i+1
                b = False

    ycord = (starth+endh)//2
    print(ycord, xcord)