for i in range(int(input())):
    n,b,x,y = list(map(int, input().split()))

    sum = 0
    cur = 0
    for i in range(n):
        if cur+x <= b: cur += x
        else: cur -= y
        sum += cur
    
    print(sum)