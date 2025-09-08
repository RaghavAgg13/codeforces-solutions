n = int(input())
b = False
idx = 0
items = []
for i in range(n):
    a = input()
    if 'OO' in a and not b:
        if not b: a = a.replace('OO', '++', 1)
        b = True
    items.append(a)

print('YES' if b else 'NO')
if b:
    print(*items, sep="\n")
        