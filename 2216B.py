for i in range(int(input())):
    a,b,c = list(map(int, input().split()))

    cnt = 0

    x = min(a,c)
    a -= x
    c -= x
    cnt += x*4

    y = min(a,b)
    a -= y
    b -= y
    cnt += y*5

    z = min(b,c)
    b -= z
    c -= z
    cnt += z*6

    cnt += a*2 + (a > y) + b*3 + c*3

    print(cnt)