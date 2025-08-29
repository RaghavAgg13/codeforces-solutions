from math import sqrt
x1,y1,x2,y2 = list(map(int, input().split()))
dist2 = (x1-x2)**2 + (y1-y2)**2
dist = dist2**0.5

b = True
if dist == int(dist):
    final = dist
else:
    final = (dist2/2)**0.5

    if final != int(final):
        b = False
        print(-1)

if b:
    dist = int(dist)
    final = int(final)
    if x1 == x2:
        print(x1+dist, y1, x2+dist, y2)
    elif y1 == y2:
        print(x1, y1+dist, x2, y2+dist)
    else:
        x, y = (x1+x2)/2, (y1+y2)/2

        slope = (x2-x1)/(y1-y2)
        ch = final/sqrt(2)
        s1 = abs(slope)/slope*sqrt(slope**2/(1+slope**2))*ch
        c1 = 1/sqrt(1+slope**2)*ch

        x3 = round(x + s1)
        y3 = round(y + c1)

        x4 = round(x - s1)
        y4 = round(y - c1)

        if abs(slope) == 1:
            print(x3,y3,x4,y4)
        else: print(-1)