for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()

    x, y = a.index(n), a.index(1) 
    
    impossible = False
    if s[0] == '1' or s[n-1] == '1':
        impossible = True
    
    if not impossible:
        if s[y] == '1' or s[x] == '1': 
            impossible = True

    if impossible:
        print(-1)
        continue
    
    mn = y + 1
    mx = x + 1

    print(5)
    print(1, mn)
    print(1, mx)
    print(mn, n)
    print(mx, n)
    print(min(mn, mx), max(mn, mx))