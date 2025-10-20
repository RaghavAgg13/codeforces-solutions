for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    check = True
    for i in range(n):
        if not (a[i] == b[i] or a[i]+1 == b[i]):
            check = False
            break

    print('YES' if check else 'NO')