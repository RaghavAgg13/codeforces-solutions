n,m = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = a[0]
count = 0
for i in range(1, n):
    cnt += a[i]
    if cnt > m:
        count += 1
        cnt = a[i]
    elif cnt == m:
        count += 1
        cnt = 0

if 0 < cnt <= m:
    count += 1

print(count)