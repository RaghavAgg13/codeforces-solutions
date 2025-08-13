n,x = list(map(int, input().split()))

count = 0
for i in range(n):
    a = input()
    if a[0] == '+': x += int(a[2:])
    else:
        if x >= int(a[2:]):
            x -= int(a[2:])
        else: count += 1

print(x, count)