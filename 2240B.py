mod = 998244353
for _ in range(int(input())):
    n,m,r,c = list(map(int, input().split()))


    E = (r*c-1) + (n-r)*(c-1) + (m-c)*(r-1)
    E %= (mod-1)

    ans = pow(2, E, mod)
    print(ans)