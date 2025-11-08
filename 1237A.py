a = []
n = int(input())

for i in range(n):
    a.append(int(input()))

count_odd = 0
for i in range(n):
    if a[i]%2: count_odd += 1

cur = 0
for i in range(n):
    if a[i]%2:
        if cur*2 < count_odd:
            print(a[i]//2+a[i]%2)
            cur += 1
        else:
            print(a[i]//2)
    else:
         print(a[i] // 2)

