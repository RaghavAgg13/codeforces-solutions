for i in range(int(input())):
    n,m,k = list(map(int, input().split()))

    cost = min((n-1) + (m-1)*n, (n-1)*m + m-1)
    print('YES' if cost == k else 'NO')