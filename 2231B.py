for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    m = 0
    for i in range(1, n):
        m = max(a[i-1]-a[i], m)

    for i in range(1, n):
        if a[i-1] > a[i]:
            a[i] += m
            if a[i-1] > a[i]:
                cnt = 100
                break
        
    print("NO" if cnt > 1 else "YES")