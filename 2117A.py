for i in range(int(input())):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    if a[a.index(1):a.index(1)+x].count(0) <= x and 1 not in a[a.index(1)+x:]:
        print('YES')
    else: print('NO')