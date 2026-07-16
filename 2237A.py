for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cost = a[0]
    prev = a[0]
    for i in range(1, n):
        if a[i] >= prev:
            cost += prev
        else:
            prev = a[i]
            cost += a[i]
        
    print(cost) 
