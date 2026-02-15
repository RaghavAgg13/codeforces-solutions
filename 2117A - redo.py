for i in range(int(input())):
    n,x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    l,r = 0, n-1
    while l < n and arr[l] == 0: l += 1
    while r > 0 and arr[r] == 0: r -= 1
    
    if (r-l+1 > x): print("NO") 
    else: print("YES")