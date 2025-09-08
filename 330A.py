r,c = list(map(int, input().split()))
pos = []

count = 0
for i in range(r):
    a = input()
    if 'S' not in a:
        count += c
        a = '#'*c
    pos.append(a)

for i in range(c):
    a = [pos[j][i] for j in range(r)]
    if 'S' not in a: count += a.count('.')

print(count)

