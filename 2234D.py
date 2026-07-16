for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    a = int(input(), 2)
    b = int(input(), 2)

    memo = {}

    def solve(a,b, k):
        key = (a, b, k) if a < b else (b, a, k)
        if key in memo:
            return memo[key]
        
        if k == 0:
            x = bin(a).count('1'); x = x*(n-x)
            y = bin(b).count('1'); y = y*(n-y)
            memo[key] = x + y
            return memo[key]
        
        if k == 1:
            x,y,z = a,b,a^b
            x = bin(x).count('1'); x = x*(n-x)
            y = bin(y).count('1'); y = y*(n-y)
            z = bin(z).count('1'); z = z*(n-z)
            memo[key] = x+y+z
            return memo[key]

        c = a ^ b
        sa = bin(a).count('1'); sa = sa*(n-sa)
        sb = bin(b).count('1'); sb = sb*(n-sb)
        sc = bin(c).count('1'); sc = sc*(n-sc)

        memo[key] = 2*solve(a,b,k-2) + solve(a,c, k-2) + solve(b,c, k-2) - (sa+sb+sc)
        return memo[key]

    print(solve(a,b,k))