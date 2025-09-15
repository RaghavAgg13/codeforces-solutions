for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    min_o = 0
    min_e = 0

    max_o = n-1
    max_e = n-1

    a.sort()
    check_1 = 0
    check_2 = 0
    for j in range(n):
        i = a[j]
        if i%2 and not check_1:
            min_o = j
            check_1 = 1
        elif not i%2 and not check_2:
            min_e = j
            check_2 = 1

        if check_1 and check_2: break

    a.sort(reverse=True)
    check_1 = 0
    check_2 = 0
    for j in range(n):
        i = a[j]
        if i%2 and not check_1:
            max_o = j
            check_1 = 1
        elif not i%2 and not check_2:
            max_e = j
            check_2 = 1

        if check_1 and check_2: break

    print(min(min_o+max_o, min_e+max_e))