for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            
            ans = max(ans, a[i]^a[j])
    
    print(ans)
