for i in range(int(input())):
    a,b = sorted(list(map(int, input().split())))

    area = min(max(a*2, b), a+b)**2
    print(area)
