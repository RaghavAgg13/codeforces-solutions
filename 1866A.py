n = int(input())
a = sorted(set(list(map(int, input().split()))), reverse=True)

b = abs(min(a))
for i in a:
    if abs(i) < b:
        b = abs(i)

print(b)