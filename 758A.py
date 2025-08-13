n = int(input())
s = sorted(list(map(int, input().split(' '))))
max = s[-1]
cost = 0
for i in s:
    cost += max - i
print(cost)