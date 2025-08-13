for i in range(int(input())):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
 
    sum = [a[0]]
    for i in range(1, n):
        sum.append(sum[i-1]+a[i])
    
    for i in range(q):
        l,r,k = list(map(int, input().split()))
        
        final = sum[-1]-sum[r-1]+(r-l+1)*k
        if l >= 2:
            final += sum[l-2]
 
        if final%2 == 1: print('YES')
        else: print('NO')