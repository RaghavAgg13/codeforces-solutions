for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    x,y = 1,n
    l,r = 0,n-1
    while (y>=x and arr[l] in [x,y] or arr[r] in [x,y]):
        if l < n and arr[l] == x:
            l += 1
            x += 1
        elif l < n and arr[l] == y:
            l += 1
            y -= 1
        elif r >= 0 and arr[r] == x:
            r -= 1
            x += 1
        elif r >= 0 and arr[r] == y:
            r -= 1
            y -= 1
        
    if y < x: print(-1)
    else: print(l+1, r+1)
