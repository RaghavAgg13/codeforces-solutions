for z in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dam = [0]*(n+1)
    for i in range(n): dam[a[i]] = i

    depth = -1
    time = 0

    for i in range(m):
        if dam[b[i]] <= depth: 
            time += 1
        else: 
            depth = dam[b[i]]
            time += (depth-i)*2+1
    
    print(time)
