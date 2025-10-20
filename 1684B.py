for i in range(int(input())):
    a,b,c = list(map(int, input().split()))
    m = min(a,b,c)

    print(a+b+c,b+c,c)