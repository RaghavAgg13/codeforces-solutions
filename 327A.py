n = int(input())
s = list(map(int, input().split()))
work = []

for i in range(n):
    if s[i] == 0:
        work.append(1)
    else: work.append(-1)

max_gain = work[0]
current_gain = work[0]
for i in range(1, n):
    current_gain = max(work[i], current_gain + work[i])
    max_gain = max(max_gain, current_gain)

if s.count(1) == n:
    print(n-1)
else: print(s.count(1)+max_gain)