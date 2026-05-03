for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l,r = 0,1
    cnt = 0
    while (r < n):
        x,y = min(a[l], a[r]), max(a[l], a[r])
        k = y-x
        if y%k == 0 and x%k == 0 and y//k == x//k+1:
            cnt += 1    
            
        if r+1 < n and a[r] == a[r+1]: 
            r += 1
            
        else:
            l = r
            r += 1

    print(cnt)
