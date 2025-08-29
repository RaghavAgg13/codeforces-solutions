n = int(input())
a = str(input())
b = str(input())

count = 0
for i in range(n):
    x,y = int(a[i]), int(b[i])
    count += min(abs(x-y), 10-abs(x-y))

print(count)