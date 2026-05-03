def chk(a,x):
    l,r = x,x
    while l >= 0 and r < len(a) and a[l] == a[r]:
        l -= 1
        r += 1
    
    b = sorted(set(a[l+1:r]))

    cnt = 0
    for i in range(len(b)):
        if i != b[i]: break
        cnt += 1

    return cnt

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l,r = a.index(0), n*2-a[::-1].index(0)-1
    x,y = a.index(0), n*2-a[::-1].index(0)-1

    cnt = 0
    cnt = max(cnt, chk(a,l))
    cnt = max(cnt, chk(a,r))

    while l >= 0 and r < n*2 and a[l] == a[r]:
        l -= 1
        r += 1

    while x < y and a[x] == a[y]:
        x += 1
        y -= 1

    if x < y:
        print(cnt)
        continue

    b = a[l+1:r]
    b = sorted(set(b))

    ans = 0
    for i in range(len(b)):
        if i != b[i]: break
        ans += 1

    print(max(cnt, ans))