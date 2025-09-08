from math import ceil
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(ceil(sum(a)/n))