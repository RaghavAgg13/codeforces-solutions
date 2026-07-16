from math import ceil
for _ in range(int(input())):
    n,x,y,z = list(map(int, input().split()))

    a = ceil(n/(x+y))

    b = min(z, ceil(n/x))

    if ceil(n/x) > z:
        b = z + ceil((n-z*x)/(x+10*y))

    print(min(a,b))