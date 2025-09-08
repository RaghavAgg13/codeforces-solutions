n = int(input())
a = list(map(int, input().split()))

b = [a[i] for i in range(n) if a.count(a[i])%2]
b.sort()

count = 0
for i in range(0 ,len(b), 2):
    count += b[i+1]-b[i]

print(count)