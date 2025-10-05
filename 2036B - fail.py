import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

for i in range(int(input())):
    n, k = map(int, input().split())

    a = defaultdict(int)
    for i in range(k):
        b,c = map(int, input().split())
        a[b] += c

    print(sum(heapq.nlargest(n, a.values())))