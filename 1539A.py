for i in range(int(input())):
    n,x,t = list(map(int, input().split()))
    
    d1 = min(n, t//x+1)
    diss = (d1*(d1-1))//2

    if d1 != n:
        diss += (n-d1)*(t//x)
    
    print(diss)