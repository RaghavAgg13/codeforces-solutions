for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(list(set(a))).copy()
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])

    for i in b: a.remove(i)
    b += a
    print(*b)