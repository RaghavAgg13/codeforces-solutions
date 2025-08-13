from collections import Counter
n = int(input())
locs = [int(input()) for i in range(n)]

print(len(Counter(locs)))