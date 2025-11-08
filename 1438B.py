from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = Counter(a).values()

    if max(count) > 1:
        print('YES')
    else:
        print('NO')