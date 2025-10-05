for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
 
    b = ['B']*m
    for i in range(n):
        if a[i] > m//2:
            a[i] = m-a[i]+1

        no = a[i]

        if 2*no-1 <= m and b[no-1] == 'B':
            b[no-1] = 'A'
        else:
            b[m-no] = 'A'
    
    print(*b, sep='')