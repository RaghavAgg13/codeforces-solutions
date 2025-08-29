n = int(input())
a = list(map(int, input().split()))
m = abs(a[0]-a[-1])
idx = [1,n]
for i in range(n-1):
    if abs(a[i]-a[i+1]) < m:
        m = abs(a[i]-a[i+1])
        idx = i+1,i+2
    if not m: break

print(*idx)