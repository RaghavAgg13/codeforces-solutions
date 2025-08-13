for i in range(int(input())):
    n,k = list(map(int, input().split()))
    s = list(map(int, input().split()))

    if sorted(s) == s:
        print('YES')
    else:
        if k == 1:
            print('NO')
        else:
            print('YES')