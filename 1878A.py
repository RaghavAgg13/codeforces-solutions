for i in range(int(input())):
    n,k = list(map(int, input().split()))
    s = list(map(int, input().split()))

    if k in s:
        print('YES')
    else:
        print('NO')