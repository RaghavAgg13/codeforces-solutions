from sys import stdin
input = stdin.readline  
for _ in range(int(input())):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n-1, -1, -1):
        if b[i] > a[i]: a[i] = b[i]
    for i in range(n-1, 0, -1):
        if a[i] > a[i-1]: a[i-1] = a[i]


    sum = [0]*(n+1)
    ans = []
    for i in range(1, n+1):
        sum[i] = sum[i-1]+a[i-1]

    for i in range(q):
        l,r = list(map(int, input().split()))

        ans.append(sum[r]-sum[l-1])
        
    print(*ans)