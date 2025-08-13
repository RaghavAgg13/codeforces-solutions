n = int(input())
magnets, parts = [], []
for i in range(n):
    magnets.append(input())

for i in range(1, len(magnets)):
    if magnets[i-1] != magnets[i]:
        parts.append(i-1)
print(len(parts) + 1)
