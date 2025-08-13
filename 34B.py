n, m = list(map(int, input().split()))
s = sorted(list(map(int, input().split())))
check = []
for i in s:
    if i < 0:
        check.append('T')
    else:
        check.append('F')
        break
# print(check)

if m <= n:
    nos = check.count('T')
    if nos < m:
        print(-sum(s[:nos]))
    else:
        print(-sum(s[:m]))