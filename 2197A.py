for _ in range(int(input())):
    n = int(input())

    s = 0
    for i in str(n):
        s += int(i)

    cnt = 0
    for j in range(1, 163):
        y = n+j
        if (y >= 0):
            dy = 0
            for i in str(y):
                dy += int(i)
            
            cnt += (y-dy == n)
    
    print(cnt)
        