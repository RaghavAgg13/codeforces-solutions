n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

count = 0
while a != []: 
    if a[0] <= k: 
        count += 1
        a.pop(0)
    else: break

while a != []: 
    if a[-1] <= k:
        count += 1
        a.pop(-1)
    else: break


print(count)