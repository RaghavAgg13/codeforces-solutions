import sys
from collections import deque

sys.setrecursionlimit(300000)
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    parent = [0, 0] + list(map(int, input().split()))

    adj = {}
    for i in range(2, n+1):
        p = parent[i]
        if p not in adj:
            adj[p] = deque([i])
        else:
            adj[p].append(i)

    val = [0] + list(map(int, input().split()))

    def dfs(idx):
        if idx not in adj:
            return val[idx]
        
        for x in adj[idx]:
            dfs(x)

        while val[adj[idx][0]] > val[adj[idx][-1]]:
            adj[idx].append(adj[idx].popleft())
        
        val[idx] = val[adj[idx][0]]

    dfs(1)
    
    arr = []
    def get(idx):
        if idx not in adj:
            arr.append(val[idx])
            return
        for x in adj[idx]:
            get(x)

    get(1)

    if arr == sorted(arr): print("YES")
    else: print("NO")