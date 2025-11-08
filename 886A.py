a = list(map(int, input().split()))
n = 6

s = sum(a)
if s%2:
    print("NO")
else:
    check = False
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (a[i]+a[j]+a[k]) == s//2:
                    print('YES')
                    check = True
                    break
            if check: break
        if check: break
    else:
        print("NO")