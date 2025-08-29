for i in range(int(input())):
    input()
    x,y = list(map(int, input().split()))
    a,b = list(map(int, input().split()))
    m,n = list(map(int, input().split()))

    f = abs(x-a)+abs(y-b)
    if x==a==m and min(y,b) < n < max(y,b): f += 2
    elif y==b==n and min(x,a) < m < max(x,a): f += 2

    print(f)