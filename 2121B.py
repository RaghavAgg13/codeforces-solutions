for i in range(int(input())):
    n = int(input())
    a = input()

    check = False
    for i in range(1, n-1):
        if a[i] in a[:i] or a[i] in a[i+1:]:
            check = True
            break

    print('YES' if check else 'NO')