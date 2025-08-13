n,k = list(map(int, input().split(" ")))
scores = list(map(int, input().split(" ")))
count = 0
score_to_beat = scores[k-1]
for i in range(n):
    if scores[i]>0:
        if scores[i] >= score_to_beat:
            count += 1
print(count)