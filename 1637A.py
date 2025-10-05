for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)
    check = False
    for i in range(n):
        if a[i] != b[i]:
            check = True
            break

    print('YES' if check else 'NO')