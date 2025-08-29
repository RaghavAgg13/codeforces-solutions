for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))

    if b > d or (a+d-b) < c:
        print(-1)
    else:
        print((d-b)+(a+d-b-c))