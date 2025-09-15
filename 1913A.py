for i in range(int(input())):
    a = input()
    n = len(a)

    check = 0
    for i in range(n-1):
        if a[i+1] != '0' and int(a[:i+1])<int(a[i+1:]):
            print(a[:i+1], a[i+1:])
            check = 1
            break

    if not check: print(-1)