# import random
n = int(input())
a = list(map(int, input().split()))
# s1 = sorted(list(dict.fromkeys(s)))
# n_unique = len(s1)
# scores = []
# for x in range(n):
#     s2 = []
#     score = 0
#     for i in range(n_unique):
#         # how to choose elements
#         num = random.randint(0,n_unique-1)
#         a = s1[-num-1]

#         # going through each element in unique items of s
#         # checking if not already ruled out
#         # if not ruled out add score accordingly and rule out
#         if a not in s2:
#             # print(a, 'not in', s2)
#             score += s.count(a)*(a)
#             s2.append(a)
#             if a-1 in s1:
#                 s2.append(a-1)
#             if a+1 in s1:
#                 s2.append(a+1)
#     if score not in scores:
#         scores.append(score)
# print(max(scores))


from collections import Counter

freq = Counter(a)
max_val = max(a)

dp = [0] * (max_val + 2)  # Extra space to avoid index issues

for x in range(1, max_val + 1):
    dp[x] = max(dp[x - 1], dp[x - 2] + x * freq[x])

print(dp[max_val])