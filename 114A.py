k = int(input())
l = int(input())

check = 1
cnt = 0
while l >= k:
    if l%k:
        check = 0
        break
    l = l//k
    cnt += 1

if l == 1:
    print("YES")
    print(cnt-1)
else:
    print("NO")