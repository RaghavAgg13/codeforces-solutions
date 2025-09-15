for i in range(int(input())):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()
    check = 1
    for i in range(n):
        if a[i] > a[n+i]-x:
            check = 0
            break

    print('YES' if check else 'NO')