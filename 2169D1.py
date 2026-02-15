for i in range(int(input())):
    x,y,k = list(map(int, input().split()))

    n_ = 10**12
    for _ in range(x):
        n_ -= n_//y

        if not n_ or k > n_:
            break
    
    if k > n_:
        print(-1)
        continue

    target = k
    for _ in range(x):
        left, right = 0, 2*10**12
        ans = right

        while left <= right:
            mid = left + (right-left)//2

            if mid - mid//y >= target:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        
        target = ans

    print(target)