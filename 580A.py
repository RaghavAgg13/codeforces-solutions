n = int(input())
str = list(map(int, input().split(' ')))
count = [0]

for i in range(1, n):
    if str[i] >= str[i-1]:
        count[len(count)-1] += 1
    else:
        count.append(0)

print(max(count)+1)