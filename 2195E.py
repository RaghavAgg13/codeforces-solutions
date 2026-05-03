from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(400000)

def get_e(i, tree, memo):
    if (memo[i] != -1): return memo[i]
    
    if (not tree[i]): memo[i] = 1   
    else: 
        memo[i] = (get_e(tree[i][0], tree, memo)+get_e(tree[i][1], tree, memo)+3)%1000000007

    return memo[i]

def ifs(i, tree, parent, ans, memo):
    if (i == 0): return 0
    if ans[i] != -1: return ans[i]

    ans[i] = (get_e(i, tree, memo) + ifs(parent[i], tree, parent, ans, memo))%1000000007
    return ans[i]

for i in range(int(input())):
    n = int(input())

    tree = [[] for _ in range(n + 1)]
    parents = [0] * (n + 1)
    
    tree[0] = [1]
    parents[1] = 0
    
    for i in range(1, n+1):
        a = list(map(int, input().split()))
        
        if (a != [0,0]):
            tree[i] = a
            parents[a[0]] = i
            parents[a[1]] = i

    ans = [-1]*(n+1)
    memo = [-1]*(n+1)

    result = []
    for i in range(1, n+1):
        result.append(ifs(i, tree, parents, ans, memo))

    print(*result)

