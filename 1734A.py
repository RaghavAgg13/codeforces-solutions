for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    cnt = 3000000000
    for i in range(1, n-1):
        x,y,z = a[i-1], a[i], a[i+1]

        mean = x
        cnt = min(cnt, abs(x-mean)+abs(y-mean)+(z-mean))
        mean = y
        cnt = min(cnt, abs(x-mean)+abs(y-mean)+(z-mean))
        mean = z
        cnt = min(cnt, abs(x-mean)+abs(y-mean)+(z-mean))


    print(cnt)