for i in range(int(input())):
    n,m = list(map(int, input().split()))

    if n >= m:
        print('YES' if n%2 == m%2 else 'NO')
    else:
        print('NO')