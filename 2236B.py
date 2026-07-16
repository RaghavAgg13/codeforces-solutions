for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(input())

    for i in range(n-k+1):
        if i+k < n and a[i] == '1':
            a[i] = '0'
            
            if a[i+k] == '1': a[i+k] = '0'
            else: a[i+k] = '1'

    if a == ['0']*n:
        print("YES")
    else:
        print("NO")