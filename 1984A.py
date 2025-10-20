for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] != a[-1]:
        print('YES')
        print('RB', 'R'*(n-2), sep='')
    else:
        print('NO')