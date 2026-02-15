from math import floor
n,k = list(map(int, input().split()))
a = sum(list(map(int, input().split())))

score = floor(a/n+.5)
moves = 0
while score < k:
    a += k
    n += 1
    moves += 1
    score = floor(a/n+.5)
print(moves)