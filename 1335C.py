from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = Counter(a).most_common(1)[0][1]
    c = len(set(a))-1
    c += (b>c+1)
    print(min(b, c))