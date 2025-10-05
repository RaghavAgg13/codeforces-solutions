for i in range(int(input())):
    n,m = list(map(int, input().split()))

    n1 = m*(n-1) - m
    n2 = m*m*(n-1)+(n-1) - n

    print(m*(m+1)//2 + m*n*(n-1)//2 + min(n1, n2) + m)