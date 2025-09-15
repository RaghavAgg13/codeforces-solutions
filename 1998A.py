for i in range(int(input())):
    x,y,k = list(map(int, input().split()))

    if k%2:
        for i in range(-k//2+1, k//2+1):
            print(x+i,y+i)
    else:
        for i in range(-k//2, k//2+1):
            if i != 0:
                print(x+i, y+i)