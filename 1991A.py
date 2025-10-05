for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = 0
    for i in range(0, n, 2):
        m = max(m, a[i])
    print(m)