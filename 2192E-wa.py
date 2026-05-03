for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    fa,fb,f = [0]*(n+1) ,[0]*(n+1), [0]*(n+1)

    for i in a: 
        fa[i] += 1
        f[i] += 1
    for i in b:
        fb[i] += 1
        f[i] += 1

    chk = 1
    for i in range(1, n+1):
        if f[i]%2: 
            print(-1)
            chk = 0
            break
    if (not chk): continue
    
    moves = []
    for i in range(n):
        if a[i] != b[i] and (fa[a[i]] > fb[a[i]] or fa[b[i]] < fb[b[i]]):
            fa[a[i]] -= 1
            fa[b[i]] += 1
            fb[a[i]] += 1
            fb[b[i]] -= 1

            a[i],b[i] = b[i],a[i]
            moves.append(i+1)
        
    if sorted(a) != sorted(b):
        print(-1)
    else:
        print(len(moves))
        print(*moves)