from collections import Counter
a = []
for i in range(int(input())):
    h,m = list(input().split())
    a.append(h+'-'+m)

print(Counter(a).most_common(1)[0][1])