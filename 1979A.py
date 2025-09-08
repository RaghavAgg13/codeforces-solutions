for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = max(a)
    for i in range(n-1):
        m = min(m, max(a[i], a[i+1]))

    print(m-1)