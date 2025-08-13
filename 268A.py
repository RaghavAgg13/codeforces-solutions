n = int(input())
h_t = []
g_t = []
count = 0

for i in range(n):
    s = list(map(int, input().split(' ')))
    h_t.append(s[0])
    g_t.append(s[-1])

for i in range(n):
    for j in range(n):
        if h_t[i] == g_t[j] and i != j:
            count += 1
print(count)