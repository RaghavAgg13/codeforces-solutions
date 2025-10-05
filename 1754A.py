for i in range(int(input())):
    n = int(input())
    a = input()

    check = 1
    for i in range(n):
        if a[i:].count("Q")*2 > n-i:
            check = 0
            break
    print('YES' if check else 'NO')