for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_min = [0] * n
    a_max = [0] * n
    a_min[0] = a[0]
    a_max[0] = a[0]
    for i in range(1, n):
        a_min[i] = min(a_min[i - 1], a[i])
        a_max[i] = max(a_max[i - 1], a[i])

    b_min = [0] * n
    b_max = [0] * n
    b_min[n - 1] = b[n - 1]
    b_max[n - 1] = b[n - 1]
    for i in range(n - 2, -1, -1):
        b_min[i] = min(b_min[i + 1], b[i])
        b_max[i] = max(b_max[i + 1], b[i])

    cnt = []
    for i in range(n):
            l = min(a_min[i], b_min[i])
            r = max(a_max[i], b_max[i])
            cnt.append((l, r))
    
    cnt.sort(key=lambda item: item[0], reverse=True)

    maximal = []
    min_r = 2 * n + 1
    for l, r in cnt:
        if r < min_r:
            maximal.append((l, r))
            min_r = r

    maximal.reverse()
    k = len(maximal)
    area = 0

    for m in range(k-1):
        l,r = maximal[m]
        L_, R_ = maximal[m+1]
        area += l*(R_-r)
    
    area += maximal[-1][0]*(2*n+1-maximal[-1][1])
    print(area)