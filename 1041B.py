from math import gcd
a,b,x,y = list(map(int, input().split()))

x,y = x//gcd(x,y), y//gcd(x,y)

cnt = min(a//x, b//y)
print(cnt)