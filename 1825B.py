for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = sorted(map(int, input().split()))

    if n > m: n,m = m,n

    ans1 = n*(m-1)*(a[-1]-a[0]) + (n-1)*(a[-1]-a[1])
    ans2 = n*(m-1)*(a[-1]-a[0]) + (n-1)*(a[-2]-a[0])

    print(max(ans1, ans2))