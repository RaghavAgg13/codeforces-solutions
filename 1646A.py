from math import ceil
for i in range(int(input())):
    n,s = list(map(int, input().split()))

    if s > n**2-1:
        print(ceil((s-n**2+1)/(n**2-1 if n != 1 else 1)))
    else:
        print(0)