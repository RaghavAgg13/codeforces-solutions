def tree(a, depths, start, stop, depth):
    if start > stop: return

    max_idx = max(range(start, stop+1), key=lambda i: a[i])
    depths[max_idx] = depth
    
    tree(a, depths, start, max_idx-1, depth+1)
    tree(a, depths, max_idx+1, stop, depth+1)
    

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    depths = [0]*n
    tree(a, depths, 0, n-1, 0)

    print(*depths)