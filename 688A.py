n,d = list(map(int, input().split()))

cnt = 0
ans = 0
for i in range(d):
    a = input()
    if a != '1'*n:
        cnt += 1
        ans = max(ans, cnt)
    else: cnt = 0

ans = max(ans, cnt)
print(ans)