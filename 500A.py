n,t = list(map(int, input().split()))
s = list(map(int, input().split()))

loc = {}
for i in range(1, n):
    loc[i] = s[i-1]+i

pos = 1
# print('initial pos is', pos)
while pos != t and pos in loc.keys():
    pos = loc[pos]
    # print('new pos is', pos)

print('YES' if pos == t else 'NO')