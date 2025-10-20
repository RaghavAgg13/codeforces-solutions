for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    s = []
    for i in range(n-1):
        s.append(abs(a[i]-a[i+1]))
    
    s.sort()
    print(sum(s[:n-k]))