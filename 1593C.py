for i in range(int(input())):
    n,k = list(map(int, input().split()))

    dist = n
    cnt = 0
    a = sorted(list(map(int, input().split())), reverse=True)
    for i in range(k):
        if (n-a[i]) < dist:
            dist -= n-a[i]
            cnt += 1
        else: break

    print(cnt)
