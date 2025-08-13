n, m = map(int, input().split())
s = list(map(int, input().split()))

unique_counts = [0] * n
seen = set()
for i in range(n - 1, -1, -1):
    seen.add(s[i])
    unique_counts[i] = len(seen)

for i in range(m):
    no = int(input())
    print(unique_counts[no - 1])
