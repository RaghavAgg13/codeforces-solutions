def recur(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
                
    return max_length * 2

for i in range(int(input())):
    a = input()
    b = input()

    moves = 0
    d = len(a)+len(b)
    f = recur(a,b)
    print(d-f)