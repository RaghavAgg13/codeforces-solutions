for i in range(int(input())):
    x,y,a,b = list(map(int, input().split()))

    if not (y-x)%(a+b):
        print((y-x)//(a+b))
    else:
        print(-1)