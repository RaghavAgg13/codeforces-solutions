for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for i in range(n-1):
        if a[i] < k:
            d = a[i]
            a[-1] += d
            k -= d
            a[i] = 0
        else:
            a[i] -= k
            a[-1] += k
            break

    print(*a)