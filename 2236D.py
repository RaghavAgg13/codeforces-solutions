for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()

    prev,cnt = 0,0
    lens = []
    for i in range(n-1):
        if a[i+1]-a[i] > k:
            cnt = max(cnt, i-prev+1)
            lens.append(i-prev+1)
            prev = i+1
    
    cnt = max(cnt, n-prev)
    lens.append(n-prev)

    for x in lens:
        if x%2 == 0:
            print("YES")
            break
    else:
        for i in range(1, n):
            if a[i] != a[i-1] and a[i]-a[i-1] <= k:
                print("YES")
                break
        else:
            print("NO")
