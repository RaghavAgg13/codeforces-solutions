from collections import Counter

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    counts = Counter(a)
    removed_count = 0

    for val in counts.values():
        removed_count += (val - 1)

    if removed_count % 2 != 0:
        removed_count += 1

    print(n - removed_count)