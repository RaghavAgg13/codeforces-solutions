k = int(input())
l = sorted(list(map(int, input().split())), reverse=True)

if sum(l) >= k:
    for i in range(13):
        if sum(l[:i]) >= k:
            print(i)
            break
if sum(l) < k:
    print(-1)