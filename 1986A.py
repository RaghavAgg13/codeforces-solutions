for i in range(int(input())):
    x,y,z = sorted(list(map(int, input().split())))

    l = sorted([z-y, z-x, y-x])
    print(l[0]+l[1])