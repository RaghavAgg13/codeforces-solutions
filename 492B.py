n,l = list(map(int, input().split(' ')))
pos = sorted(list(map(int, input().split(' '))))
d = 0
for i in range(1, n):
    gap = pos[i] - pos[i-1]
    if gap/2 > d:
        d = gap/2

if max(pos[0], l-pos[-1]) > d:
    d = max(pos[0], l-pos[-1])
print(d)