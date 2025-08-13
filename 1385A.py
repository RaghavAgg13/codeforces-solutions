for i in range(int(input())):
    x,y,z = list(map(int, input().split()))


    if x == y == z:
        print('YES')
        print(x,y,z)
    elif (x == y and z < x) or (y == z and x < y) or (z == x and y < z):
        print('YES')
        if x == y and z < x: print(x, z, z)
        elif y == z and x < y: print(y, x, x)
        else: print(x, y, y)
    else:
        print('NO')