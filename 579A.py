n = int(input())
count = 0
while n != 1:
    if n % 2 != 0:
        count += 1
        n = (n-1)/2
    if n % 2 == 0:
        n /= 2
else:
    count += 1
print(count)