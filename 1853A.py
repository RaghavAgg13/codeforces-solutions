from math import ceil
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    if l == sorted(l):
        soln = []
        for i in range(1, n):
            x = ceil((l[i]-l[i-1]+1)/2)
            if x not in soln: soln.append(x)
        print(min(soln))
    else:
        print(0)