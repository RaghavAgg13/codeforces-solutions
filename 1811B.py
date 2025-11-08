for i in range(int(input())):
    n,a,b,c,d = list(map(int, input().split()))

    n1 = min(a, n-a+1, b, n-b+1)
    n2 = min(c, n-c+1, d, n-d+1)

    print(abs(n1-n2))