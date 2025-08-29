for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c = sorted(a)

    check = 1
    for i in range(n):
        if a[i]%2 != c[i]%2:
            check = 0
            break

    print('YES' if check else 'NO')