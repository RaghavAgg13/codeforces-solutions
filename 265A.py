a = input()
b = input()
n = len(b)

pos = 1
for i in range(n):
    if a[pos-1] == b[i]:
        pos += 1

print(pos)