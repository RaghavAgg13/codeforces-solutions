import sys
from collections import defaultdict

input = sys.stdin.readline

for i in range(int(input())):
    n, k = map(int, input().split())

    # a = defaultdict(int)
    a = [0]*(k+1)
    for i in range(k):
        b,c = map(int, input().split())
        a[b] += c

    # brand_totals = list(a.values())
    brand_totals = a
    brand_totals.sort(reverse=True)
    print(sum(brand_totals[:n]))