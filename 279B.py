n, t = list(map(int, input().split()))
s = list(map(int, input().split()))

score = 0
count = 0
left = 0
scores = []

for i in range(n):
    score += s[i]

    while score > t:
        score -= s[left]
        left += 1

    count = max(count, i-left+1)

print(count)