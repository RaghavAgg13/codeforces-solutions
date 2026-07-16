for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.append(0)
    b.sort()

    pre = [a[0]]
    for i in range(1, n):
        pre.append(pre[-1]+a[i])

    changes = []
    for i in range(1, m+1):
        d = 0
        for j in range(b[i-1], b[i]):
            d += a[j]
        changes.append(d)

    sum = 0
    for i in changes: sum += abs(i)

    for i in range(b[-1], n): sum += a[i]

    print(sum)