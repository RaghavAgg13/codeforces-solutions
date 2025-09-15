for i in range(int(input())):
    n = int(input())
    a = input()

    check = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            print(i+1, i+2)
            check = 1
            break

    if not check: print('-1 -1')