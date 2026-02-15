for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = n
    for i in range(n-1):
        m = min(m, a[i])
        if m == n-i: 
            print('NO')
            break
    else:
        print("YES")