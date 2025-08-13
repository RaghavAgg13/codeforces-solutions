n = int(input())
s = list(map(int, input().split()))

score = 1
count = 1
for i in range(1, n):
    if s[i] > s[i-1]:
        count += 1
    else:
        if score < count: score = count
        count = 1
    
if score < count: score = count
print(score)