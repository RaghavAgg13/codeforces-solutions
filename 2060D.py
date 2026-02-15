for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-1):
        m = min(a[i], a[i+1])
        a[i] -= m
        a[i+1] -= m

    print('YES' if a == sorted(a) else 'NO')