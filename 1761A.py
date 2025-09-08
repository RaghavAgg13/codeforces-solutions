for i in range(int(input())):
    n,a,b = list(map(int, input().split()))

    if a+b <= n-2 or n==a==b: print('Yes')
    else: print('No')