n = int(input())
a = input()
# Complexity O((n/2)**2)
# pos = list(map(int, input().split()))
# left, right = set(), set()
# for i in range(n):
#     if a[i] == 'L': left.add(pos[i])
#     else: right.add(pos[i])

# # print(left, right)
# left, right = sorted(left), sorted(right)

# if left[-1] < right[0]: print(-1)
# else:
#     dist = 1000000000
#     for i in left:
#         for j in right:
#             if i > j:
#                 dist = min(dist, (i-j)//2)
#         if dist == 1: break

#     print(dist)



# Complexity O(n)?
from sys import stdin, stdout
input = stdin.readline
pos = input().split()

right, left = 1000000000, 0
dist = 1000000000
for i in range(n):
    if a[i] == 'R': right = int(pos[i])
    else: left = int(pos[i])

    if left > right:
        dist = min(dist, (left-right)//2)

# print(dist if dist != 1000000000 else -1)
stdout.write(str(dist) if dist != 1000000000 else "-1")