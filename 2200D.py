for i in range(int(input())):
    n,x,y = list(map(int, input().split()))
    a = list(map(int, input().split()))

    m = a.index(min(a[x:y]))

    if 1 in a[x:y]:
        a = a[m:y] + a[x:m] + a[:x] + a[y:]
    else:
        b = a[m:y] + a[x:m]
        s = a[:x] + a[y:]
        k = 0
        while k < len(s) and s[k] < b[0]:
            k += 1
        a = s[:k] + b + s[k:]

    print(*a)