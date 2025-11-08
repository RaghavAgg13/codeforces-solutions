for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0]*n

    for i in range(n-1, -1, -1):
        next_idx = i+a[i]

        if next_idx < n:
            dp[i] = a[i]+dp[next_idx]
        else:
            dp[i] = a[i]

    maxSum = max(dp)
    print(maxSum)