for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    # print(a)

    target = a[n//2]

    cnt = 0
    l,r = 0,n-1
    while l < r:
        if a[l] == target and a[r] == target: break

        l += 1
        r -= 1
        cnt += 1
    
    print(cnt)
