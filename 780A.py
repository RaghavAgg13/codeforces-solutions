from sys import stdin
input = stdin.readline

n = int(input())

count = 0
final = 0
table = set()
a = list(map(int, input().split()))
for i in a:
    if i not in table:
        table.add(i)
        count += 1
    else: 
        table.remove(i)
        final = max(final, count)
        count -= 1
print(final)