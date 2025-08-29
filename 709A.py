n,b,d = list(map(int, input().split()))
a = list(map(int, input().split()))

stock = 0
count = 0
for i in a:
    if i <= b:
        stock += i
        if stock > d:
            stock = 0
            count += 1

print(count)