for _ in range(int(input())):
    n,x,s = list(map(int, input().split()))
    a = input()

    l,r,ans = 0,0,0

    for i in a:
        if i == "I":
            if l == x: continue

            ans += 1
            l += 1
            r = min(x, r+1)
        elif i == "E":
            if r*s == ans: continue

            ans += 1
            if ans > l*s: l += 1
        else:
            if x*s == ans: continue

            ans += 1
            if ans > l*s: l += 1
            r = min(x, r+1)
    
    print(ans)