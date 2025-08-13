n,k = map(int, input().split())
s = list(map(int, input().split()))

min_sum = curr_sum = sum(s[:k])
index = 0
target_min = min(s) * k

for i in range(1, n - k + 1):
    curr_sum += s[i + k - 1] - s[i - 1]
    
    if curr_sum < min_sum:
        min_sum = curr_sum
        index = i

        if min_sum == target_min: break

print(index + 1)