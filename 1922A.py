for i in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = input()

    check = True
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            check = False
            break

    print('YES' if not check else 'NO')