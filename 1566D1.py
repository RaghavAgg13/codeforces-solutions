for i in range(int(input())):
    m,n = list(map(int, input().split()))
    a = list(map(int, input().split()))

    inc = sum(map(lambda i: sum(1 for j in range(i) if a[j] < a[i]), range(1, n)))
    
    print(inc)