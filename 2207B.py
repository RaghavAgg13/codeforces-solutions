for _ in range(int(input())):
    n,m,l = list(map(int, input().split()))
    a = list(map(int, input().split()))

    dangers = [0]*m
    cur = 0
    for i in range(l):
        dangers[m-min(m, n-cur+1)] += 1
        dangers.sort()

        if cur < n:
            if a[cur]-1 == i:
                dangers[-1] = 0
                dangers.sort()
                cur += 1
        else:
            dangers[-1] += (l-i-1)
            break 
    
    print(dangers[-1])