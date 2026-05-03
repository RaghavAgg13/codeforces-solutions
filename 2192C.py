for i in range(int(input())):
    n,h,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    s = sum(a)

    time = n*((h-1)//s) + k*((h-1)//s)
    h -= ((h-1)//s)*s 

    suf_max = [0]*(n+1)
    for j in range(n-1, -1, -1):
        suf_max[j] = max(suf_max[j+1], a[j])

    cum_sum = 0
    min_so_far = float('inf')
    
    for j in range(n):
        cum_sum += a[j]
        min_so_far = min(min_so_far, a[j])
        
        best_sum = cum_sum
        if suf_max[j+1] > min_so_far:
            best_sum += suf_max[j+1] - min_so_far
        
        if best_sum >= h:
            print(time +j+1)
            break