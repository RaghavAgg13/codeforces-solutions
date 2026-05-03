for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()
    for i in range(n-1, 0, -1):
        a[i] -= a[i-1]
    idx = 0

    moves = 0
    while (k > 0 and idx < n):
        p = min(k, a[idx]*(n-idx))

        k -= p
        moves += p

        if (p < a[idx]*(n-idx)): a[idx] -= p//(n-idx)
        else: 
            idx += 1
            if not k: break
            moves += 1
    
    print(moves)