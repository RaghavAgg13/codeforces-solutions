for i in range(int(input())):
    a,b = 0,0
    for i in range(int(input())):
        x,y = list(map(int, input().split()))
        a = max(a, x)
        b = max(b, y)
    
    print(2*a+2*b)