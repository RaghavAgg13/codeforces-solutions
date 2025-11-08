from math import ceil
for i in range(int(input())):
    l,r,d = list(map(int, input().split()))

    ans = ceil((r+1)/d)*d
    b = min((l//d)*d, d)
    print(b if b > 0 and b < l and b < ans else ans)
