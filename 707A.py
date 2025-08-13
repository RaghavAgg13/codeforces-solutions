n, m = list(map(int, input().split()))
s = []
b = False
for i in range(n):
    a = list(map(str, input().split()))
    s += a
s = list(set(s))

for i in ['C', 'M', 'Y']:
    if i in s:
        b = True

print('#Color' if b else '#Black&White')