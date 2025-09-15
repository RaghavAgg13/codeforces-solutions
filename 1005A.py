n = int(input())
a = list(map(int, input().split()))

count = 0
lengths = []
for i in range(n-1):
    if a[i] >= a[i+1]:
        lengths.append(a[i])
        count += 1
lengths.append(a[-1])

print(count+1)
print(*lengths)