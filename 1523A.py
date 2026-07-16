for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(input())

    ids = []
    if a[0] == '0' and a[1] == '1': ids.append(0)
    if a[n-1] == '0' and a[n-2] == '1': ids.append(n-1)
    for i in range(1, n-1):
        if a[i] == '0' and (int(a[i-1])+int(a[i+1]) == 1):
            ids.append(i)
    
    for i in range(m):
        if len(ids) == 0:
            break

        for idx in ids:
            a[idx] = '1'

        ids = []
        if a[0] == '0' and a[1] == '1': ids.append(0)
        if a[n-1] == '0' and a[n-2] == '1': ids.append(n-1)
        for i in range(1, n-1):
            if a[i] == '0' and (int(a[i-1])+int(a[i+1]) == 1):
                ids.append(i)
    
    print(''.join(a))
