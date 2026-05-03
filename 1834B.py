for i in range(int(input())):
    l,r = list(map(str, input().split()))

    n1,n2 = len(l), len(r)

    if (n1 > n2):
        r = (n1-n2)*'0' + r
    elif (n1 < n2):
        l = (n2-n1)*'0' + l


    idx = 0
    n = max(n1, n2)

    while (idx < n):
        if (l[idx] == r[idx]): idx += 1
        else: break
    
    ans = max(0, (n-idx-1)*9)
    if idx < n: ans += abs(int(l[idx])-int(r[idx]))
    print(ans)
