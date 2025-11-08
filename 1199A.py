n,x,y = list(map(int, input().split()))
a = list(map(int, input().split()))

start, end = a[0], a[-1]
for i in range(x): a.insert(0, start)
for i in range(y): a.insert(-1, end)

for i in range(1, n+x+y):
    if a[i] > a[i-1]: a[i] = a[i-1]

for i in range(x, n+x):
    if a[i-x] >= a[i] <= a[i+y]:
        print(i-x+1)
        break