for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    check = 1
    diff = 0
    for i in range(n):
        if a[i] > b[i]:
            diff = max(diff, a[i]-b[i]  )

    for i in range(n):
        if max(a[i]-diff, 0) != b[i]: 
            check = 0
            print('NO')
            break

    if check: print('YES')