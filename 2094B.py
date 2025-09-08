for i in range(int(input())):
    n,m,l,r = list(map(int, input().split()))

    print(l+(n-m-min(n-m, r)), r-min(n-m, r))