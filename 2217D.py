
for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    x = a[p[0]-1]
    
    c = [0]*(n+2)
    for i in range(1, n+1):
        c[i] = 1 if a[i-1] != x else 0
        
    d = [0]*(n+2)
    for i in range(1, n+2):
        d[i] = c[i]^c[i-1]
        
    p_full = [0]+p+[n+1]
    
    M,S = 0,0
    for i in range(len(p_full)-1):
        start = p_full[i] + 1
        end = p_full[i+1]
        
        cnt = sum(d[start : end+1])
        if cnt > M: M = cnt
        S += cnt
        
    ans = max(S//2, M)
    print(ans)

