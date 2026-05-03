for i in range(int(input())):
    n,c,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()
    
    if (a[0] > c): print(c)
    else:
        used = min(k, c-a[0])
        c += a[0] + used
        k -= used
        for i in range(1, n):
            if (a[i] <= c):
                used = min(k, c-a[i])
                c += a[i] + used
                k -= used
            else:
                break
        
        print(c)