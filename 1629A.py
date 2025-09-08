for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = [[a[i],b[i]] for i in range(n)]
    d = sorted(d, key=lambda x: x[0])

    for a,b in d:
        if a <= k: k += b
        else: break

    print(k)