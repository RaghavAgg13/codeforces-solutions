for i in range(int(input())):
    n,d = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))

    print('YES' if a[0]+a[1] <= d or max(a) <= d else 'NO')