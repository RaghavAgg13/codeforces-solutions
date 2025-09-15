for i in range(int(input())):
    a,b,c = sorted(list(map(int, input().split())))

    d = abs(a+c-b*2)
    print(1 if d%3 else 0)