for i in range(int(input())):
    n,m,k,h = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    a = sum([1 if not abs(i-h)%k and i != h and abs(i-h)//k < m else 0 for i in a])
    print(a)