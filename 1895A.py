for i in range(int(input())):
    x,y,k = list(map(int, input().split()))


    if y < x: print(x)
    else: print(x+k+(y-x-k)*2 if y-x-k+1>0 else y)