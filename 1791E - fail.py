for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    for attempt in range(n-1):
        lowest = max(a)*2
        idx = 0
        for i in range(n-1):
            d = (a[i]+a[i+1])
            if d < lowest:
                lowest = d
                idx = i

        if lowest < 0:
                a[idx] *= -1
                a[idx+1] *= -1

    if n == 2 and sum(a) < 0:
        print(-sum(a))
    else:
        print(sum(a))