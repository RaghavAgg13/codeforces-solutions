n,m = list(map(int, input().split(' ')))
b = False
l1 = []
for i in range(n):
    row = [2]*m
    l1.append(row)

for i in l1:
    for j in range(m):
        if i[j] != 0:
            b = not b
            i[j] = 0
            i = [0]*m
            for x in range(n):
                (l1[x])[j] = 0

print('Akshat' if b else 'Malvika')