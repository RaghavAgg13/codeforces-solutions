n,x = list(map(int, input().split()))
f = []

count = 0
i = 1
while i * i <= x:
    if x % i == 0:
        j = x // i
        if i <= n and j <= n:
            count += 1
        if i != j and j <= n and i <= n:
            count += 1
    i += 1

print(count)