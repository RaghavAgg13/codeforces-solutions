from math import sqrt
for i in range(int(input())):
    x,y = list(map(int, input().split()))

    dist = sqrt(x**2+y**2)
    if x == y == 0: print(0)
    elif dist == int(dist): print(1)
    else: print(2)
