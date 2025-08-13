s, n =list(map(int, input().split(' ')))
b = False
diff = []
for i in range(n):
    xi, yi = list(map(int, input().split(' ')))
    diff.append([xi, yi])

diff = sorted(diff)
# print(diff)
for i in range(n):
    if s > diff[i][0]:
        s += diff[i][1]
        b = True
    else:
        b = False
        break

if b: print('YES')
else: print('NO')