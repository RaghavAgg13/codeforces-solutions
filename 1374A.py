t = int(input())

for i in range(t):
    x,y,n = list(map(int, input().split()))

    if n < x:
        print(y)
    else:    
        print(((n - y) // x) * x + y)