freq = [0]*1001
n,k = list(map(int, input().split()))

for i in range(n):
    a = int(input())
    freq[a] += 1

cnt = 0
odd = 0
for i in freq:
    cnt += i-i%2
    if i%2: odd += 1

cnt += odd//2+odd%2
print(cnt)