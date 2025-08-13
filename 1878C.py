for i in range(int(input())):
    n,k,x = list(map(int, input().split()))

    if n*(n+1)//2 - (n-k)*(n-k+1)//2 >= x and k*(k+1)//2 <= x:
        print('YES')
    else: print('NO')