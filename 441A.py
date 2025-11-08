n,v = list(map(int, input().split()))

cnt = 0
sellers = []
for i in range(n):
    a = list(map(int, input().split()))

    m = min(a[1:])
    if m+1 <= v:
        cnt += 1
        sellers.append(i+1)

print(cnt)
print(*sellers)