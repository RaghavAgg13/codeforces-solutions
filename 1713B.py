for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)

    check = True
    left, right = 0, n-1
    cnt = 0
    while cnt < n:
        if a[left] == b[cnt]:
            left += 1
            cnt += 1
        elif a[right] == b[cnt]:
            right -= 1
            cnt += 1
        else:
            check = False
            break
    
    print('YES' if check else 'NO')