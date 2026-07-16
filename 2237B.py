for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_ = sorted(a)
    for i in range(n):
        if a_[i] > b[i]:
            print(-1)
            break
    else:
        # solution gauranteed to exist

        cost = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i] > b[j]:
                    cost[i].append(1e9)
                else:
                    cost[i].append(b[j]-a[i])
        
        ans, left = 0,0

        while left < n:
            idx_l = 0
            
            for j in range(n):
                if cost[j][left] < 1e9:
                    idx_l = j
                    break

            for j in range(idx_l+1, n):
                if cost[j][n-1] == 1e9:
                    ans += 1
            
            cost[idx_l] = [1e9]*n
            left += 1
        
        print(ans)