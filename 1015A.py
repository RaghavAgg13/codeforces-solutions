n,m = list(map(int, input().split()))

nos = [i+1 for i in range(m)]
count = m
for i in range(n):
    l,r = list(map(int, input().split()))

    for i in range(l, r+1):
        if i in nos: 
            nos.remove(i)
            count -= 1

print(count)
print(*nos)