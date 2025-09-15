for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = 0
    for i in set(a):
        if a.count(i) >= 2:
            check = 1
            break

    print('YES' if check else 'NO')