for i in range(int(input())):
    n,k = list(map(int, input().split()))

    if k >= n-1:
        print(1)
    else:
        count = 0
        while n-count-1 <= k and n-count-1>0:
            k -= n-count
            count += 1
        
        print(n-count)