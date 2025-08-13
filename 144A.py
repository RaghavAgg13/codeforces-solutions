n = int(input())
heights = list(map(int, input().split(' ')))
h_max, h_min = 0,0

beta = []
for i in range(n):
    if heights[i] == max(heights):
        beta.append(i)
h_max = min(beta)

count = h_max

for i in range(count):
    c = heights[h_max-1]
    heights[h_max-1] = heights[h_max]
    heights[h_max] = c
    h_max -=1

alpha = []
for i in range(n-1, 0, -1):
    if heights[i] == min(heights):
        alpha.append(i)
h_min = max(alpha)

count += len(heights) - h_min - 1

print(count)