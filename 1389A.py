from math import gcd
for i in range(int(input())):
    l,r = list(map(int, input().split()))

    if l*2 > r:
        print('-1 -1')
    else: 
        print(l, l*2)