from math import ceil
n,d = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))

# print(a)

b = []
for i in a:
    b.append(ceil((d+1)/i))
# print(b)

b.reverse()
cnt = 0
count = 0
for i in b:
    count += i
    if count <= n:
        cnt += 1
    
    if count >= n: break

print(cnt)