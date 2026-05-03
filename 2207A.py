for i in range(int(input())):
    n = int(input())
    a = list(input())

    z = []
    for i in range(1, n-1):
        if a[i] == '0' and a[i-1] == '1' and a[i+1] == '1':
            a[i] = '1'
    
    n1 = a.count('1')

    cnt, l = 0, 0
    for i in range(n):
        if a[i] == '1':
            l += 1
        else:
            if l >= 3: cnt += (l-1)//2
            l = 0

    if (l >= 3): cnt += (l-1)//2
    
    print(n1-cnt, n1)