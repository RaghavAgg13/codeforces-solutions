import bisect
n = int(input())
s = list(map(int, input().split()))

cull_s = [s[0]]
for i in range(1, n):
    cull_s.append(s[i]+cull_s[i-1])

m = int(input())
l = list(map(int, input().split()))

for i in l:
    print(bisect.bisect_left(cull_s, i)+1)