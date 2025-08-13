for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = True
    for i in range(1,n):
        b = abs(a[i]-a[i-1])
        if b not in [5, 7]:
            check = False
            break
    
    print('YES' if check else 'NO')