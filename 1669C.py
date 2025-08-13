for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    oddc = [a[i]%2 for i in range(0, n, 2)]
    evenc = [a[i]%2 for i in range(1, n, 2)]

    if len(set(oddc)) == 1 and len(set(evenc)) == 1:
        print('YES')
    else:
        print('NO')