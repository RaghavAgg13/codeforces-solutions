for i in range(int(input())):
    n,k = list(map(int, input().split()))

    a = min(n-k, k)
    print('1'*a, '0'*(n-k-a), '1'*(k-a), '0'*a, sep='')