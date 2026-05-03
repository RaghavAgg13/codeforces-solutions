for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l,r = 0,0
    chk = 0
    for i in range(1, n):
        if a[i] == a[i-1]:
            r += 1
        else:
            if (l == 0 or a[l] < a[l-1]) and a[r] < a[i]:
                chk += 1
            l = r = i
        
    if l == 0 or a[l] < a[l-1]:
        chk += 1

    print("YES" if chk==1 else "NO")