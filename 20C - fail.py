n,m = list(map(int, input().split()))
f = []
t = []
dist = []
b = True
for i in range(m):
    a,b,w = list(map(int, input().split()))
    f.append(a)
    t.append(b)
    dist.append(w)

if n in t:
    pos = [[f[i], t[i]] for i in range(m)]
    paths = []
    solns = []
    for i in range(m):
        if pos[i][0] == 1:
            path = [pos[i]]
            paths.append(path)

    for path in paths:
        for i in range(10):
            for po in pos:
                if po[0] == path[-1][-1]:
                    path.append(po)
        if path[-1][-1] != n and len(paths) == 1:
            print(-1)
            b = False

    if not b:
        for path in paths:
            soln = 0
            for pat in path:
                soln += dist[pos.index(pat)]
            solns.append(soln)

        final = paths[solns.index(min(solns))]
        for i in final: print(i[0], end=' ')
        print(n)
else: print(-1)