n = int(input())
a = list(map(int, input().split()))
m = int(input())

a.insert(0, 0)
a.insert(n+1, 0)
for i in range(m):
    x,y = list(map(int, input().split()))

    a[x-1] += y-1
    a[x+1] += a[x]-y
    a[x] = 0

for i in range(1, n+1):   
    print(a[i])
