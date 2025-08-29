for i in range(int(input())):
    a = list(map(int, input().split()))
    a += list(map(int, input().split()))


    if a[0] < a[1] < a[3] and a[0] < a[2] < a[3]:
        print('YES')
    elif a[2] < a[0] < a[1] and a[2] < a[3] < a[1]:
        print('YES')
    elif a[3] < a[2] < a[0] and a[3] < a[1] < a[0]:
        print('YES')
    elif a[1] < a[3] < a[2] and a[1] < a[0] < a[2]:
        print('YES')
    else:
        print('NO')
