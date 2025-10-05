for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = 0
    if a.count(1) > n-1: check = 1

    if not check:
        for i in range(n-1):
            if a[i] == a[i+1] == 0:
                check = 1
                break

    print('YES' if check else 'NO')