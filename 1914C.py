for i in range(int(input())):
    n,k = list(map(int, input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    check = [False]*n
    
    score = a[0]
    b = [max(b[:i+1]) for i in range(n)]
    
    for i in range(k-1):
        if check[::-1].index(True) 