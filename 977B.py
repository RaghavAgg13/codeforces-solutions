from collections import Counter
n = int(input())
l = input()

g2 = []
for i in range(n-1):
    g2.append(l[i:i+2])

count = Counter(g2)
print(count.most_common(1)[0][0])