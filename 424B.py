from math import sqrt
n,p = list(map(int, input().split()))
a = []

for i in range(n):
    x,y,z = list(map(int, input().split()))
    r = sqrt(x**2 + y**2)
    a.append([r, z])

a.sort()

for i in range(1, n):
    a[i][1] += a[i-1][1]

if a[-1][1]+p < 1000000:
    print(-1)
else:
    l,r = 0, n-1
    ans = -1

    while (l <= r):
        mid = l + (r-l)//2

        if (a[mid][1] >= 1000000-p):
            ans = a[mid][0]
            r = mid-1
        else:
            l = mid+1

    print(ans)