for i in range(int(input())):
    n,m,r_,c_,r,c = list(map(int, input().split()))

    w1 = r-r_
    if r < r_:
        w1 += 2*(n-r)
        if r_ == n: w1 = abs(w1)
        
    w2 = c - c_
    if c < c_:
        w2 += 2*(m-c)
        if c_ == m: w2 = abs(w2)
    
    print(min(w1,w2))