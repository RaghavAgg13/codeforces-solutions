for i in range(int(input())):
    k,x = list(map(int, input().split()))

    x *= 2**k
    
    print(x)