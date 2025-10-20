for i in range(int(input())):
    n = int(input())

    maxy, miny = 0, 0
    maxx, minx = 0, 0

    for i in range(n):
        x,y = list(map(int, input().split()))

        miny = min(miny, y)
        maxy = max(maxy, y)
        minx = min(minx, x)
        maxx = max(maxx, x)
    
    
    print(2*(-minx-miny+maxx+maxy))