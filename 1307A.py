for _ in range(int(input())):
    n,d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    pos = 1
    while (pos < n):
        m = min(pos*a[pos], d)
        a[0] += m//pos

        d -= m
        pos += 1
        if (d == 0): break
    
    print(a[0])
