for i in range(int(input())):
    a = input()
    b = input()
    n = len(a)

    check = False
    for i in range(0, n, 2):
        if a[i] == b:
            check = True
            break

    print('YES' if check else 'NO')