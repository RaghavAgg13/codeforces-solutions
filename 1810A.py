for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = 0
    for i in range(n):
        if a[i] <= i+1:
            check = 1
            break
    print('YES' if check else 'NO')