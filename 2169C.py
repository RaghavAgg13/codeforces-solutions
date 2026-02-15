for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    p = [0]*(n+1)

    for i in range(n):
        p[i+1] = p[i] + a[i]
    
    org_sum = p[n]

    gain = 0
    cul_gain_g = 0
    for r in range(1, n+1):
        g = p[r-1] - r*r + r
        cul_gain_g = max(g, cul_gain_g)

        f = r*r + r - p[r]
        cur_gain = f + cul_gain_g

        gain = max(gain, cur_gain)
    
    print(org_sum + gain)