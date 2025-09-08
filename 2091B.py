for i in range(int(input())):
    n,x = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())), reverse=True)

    count = 0
    start = 0
    for i in range(n):
        delta = min(a[start:i+1])*(i-start+1)
        if delta >= x:
            count += 1
            start = i+1
    
    print(count)