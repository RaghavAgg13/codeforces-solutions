n = int(input())
a = list(map(int, input().split()))

count = 0
i = 0
while count < n:
    count += a[i%7]
    i += 1

print(i%7 if i%7 != 0 else 7)