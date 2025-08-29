from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(n-max(Counter(a).values()))