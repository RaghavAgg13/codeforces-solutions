for i in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    arr = [[-1] for _ in range(k+1)]

    # add distances corresponding to a certain color
    for i in range(n): arr[a[i]].append(i)

    # pad with n - last plank to n can be split
    for i in range(1, k+1): arr[i].append(n)

    # generate diff array
    dist = [[] for _ in range(k+1)]
    ans = float('inf')

    for i in range(1, k+1):
        l = len(arr[i])
        for j in range(1, l):
            dist[i].append(arr[i][j] - arr[i][j-1] - 1)

        dist[i].sort()
        
        if len(dist[i]) > 0:
            mx1 = dist[i][-1]
            mx2 = dist[i][-2] if len(dist[i]) > 1 else 0
            # split max and compare with 2nd largest
            ans = min(ans, max(mx1//2, mx2))

    print(ans)