for _ in range(int(input())):
    n = int(input())

    adj = []
    chk = False

    for i in range(n):
        a = input()
        adj.append(list(a))

        if a[i] == '0': chk = True
        
    if chk: 
        print("NO")
        continue

    for u in range(n):
        for v in range(n):
            if (u == v): continue

            if (adj[u][v] == '1' and adj[v][u] == '1'):
                chk = True
                break
            
            if adj[u][v] == '0':
                for w in range(n):
                    if adj[u][w] == '1' and adj[w][v] == '1':
                        chk = True
                        break
        if chk: break

    if chk: 
        print("NO")
        continue

    edges = []
    for u in range(n):
        for v in range(n):
            if u == v or adj[u][v] == '0': continue

            for w in range(n):
                if u == w or v == w: continue

                if adj[u][w] == '1' and adj[w][v] == '1':
                    break
            else:
                edges.append([u+1,v+1])
    
    if len(edges) == n-1:
        p = list(range(n+1))
        for u, v in edges:
            while p[u] != u: u = p[u]
            while p[v] != v: v = p[v]
            p[u] = v
            
        if sum(1 for i in range(1, n + 1) if p[i] == i) == 1:
            print("YES")
            for edge in edges:
                print(*edge)
        else:
            print("NO")
    else:
        print("NO")