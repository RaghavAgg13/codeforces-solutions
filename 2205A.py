for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = a.index(max(a))

    a[0],a[m] = a[m], a[0]
    print(*a)