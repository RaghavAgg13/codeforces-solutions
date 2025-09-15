for i in range(int(input())):
    n = int(input())

    upper = input()
    lower = input()

    check = True
    for i in range(1, n):
        if upper[i] == "1" and lower[i] == "1":
            check = False
            break

    print('YES' if check else 'NO')