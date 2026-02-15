for i in range(int(input())):
    n,l,r = list(map(int, input().split()))
    a = list(map(int, input().split()))

    sum, count, left = 0, 0, 0
    
    for i in range(n):
        sum += a[i]

        while sum > r and left < n:
            sum -= a[left]
            left += 1
            
        if l <= sum <= r:
            count += 1
            sum = 0
            left = i+1
        

    print(count)