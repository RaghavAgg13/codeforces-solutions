import random
from collections import deque

def solve_bf(n, k, a, p):
    x = a[p[0]-1]
    target = [x]*n
    if a == target: return 0
    
    q = deque([(tuple(a), 0)])
    vis = set([tuple(a)])
    
    while q:
        curr, dist = q.popleft()
        for i in range(n):
            for j in range(i, n):
                # check if contains special index
                valid = False
                for sp in p:
                    if i <= sp-1 <= j:
                        valid = True
                        break
                if valid:
                    nxt = list(curr)
                    for idx in range(i, j+1):
                        nxt[idx] = 1 - nxt[idx]
                    t = tuple(nxt)
                    if t not in vis:
                        if list(nxt) == target:
                            return dist + 1
                        vis.add(t)
                        q.append((t, dist+1))
    return -1

def solve_formula(n, k, a, p):
    x = a[p[0]-1]
    c = [0]*(n+2)
    for i in range(1, n+1):
        c[i] = 1 if a[i-1] != x else 0
    d = [0]*(n+2)
    for i in range(1, n+2):
        d[i] = c[i] ^ c[i-1]
        
    p_full = [0] + p + [n+1]
    regions = []
    for i in range(len(p_full)-1):
        cnt = 0
        start = p_full[i] + 1
        end = p_full[i+1]
        for j in range(start, end+1): # wait, does end+1 cover correctly?
            if d[j] == 1:
                cnt += 1
        regions.append(cnt)
    
    S = sum(regions)
    M = max(regions)
    return max(S//2, M)

def main():
    for _ in range(500):
        n = random.randint(2, 10)
        k = random.randint(1, n)
        a = [random.randint(0, 1) for _ in range(n)]
        p = random.sample(range(1, n+1), k)
        p.sort()
        # ensure all a[p_i] are the same
        x = random.randint(0, 1)
        for sp in p:
            a[sp-1] = x
            
        ans_bf = solve_bf(n, k, a, p)
        ans_f = solve_formula(n, k, a, p)
        if ans_bf != ans_f:
            print("MISMATCH!", n, k, a, p, "BF:", ans_bf, "Formula:", ans_f)
            exit(1)
    print("ALL MATCH!")

if __name__ == "__main__":
    main()
