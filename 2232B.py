for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, n):
        a[i] += a[i-1]
    
    for i in range(n):
        a[i] //= (i+1)
    
    for i in range(1, n):
        a[i] = min(a[i], a[i-1])
    
    print(* a)