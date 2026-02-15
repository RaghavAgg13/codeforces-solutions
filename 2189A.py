for i in range(int(input())):
    n,h,l = list(map(int, input().split()))

    a = sorted(list(map(int, input().split())))

    i = 0
    r = n-1
    while r > 0 and a[r] > max(h,l): r -= 1

    cnt = 0
    while (i < r):
        if a[i] <= min(h,l) and a[r] <= max(h,l):
            i += 1
            r -= 1
            cnt += 1
        else: break

    # print(a[i:r+1])
    print(cnt)
