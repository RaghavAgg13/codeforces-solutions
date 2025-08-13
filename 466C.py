n = int(input())
a = list(map(int, input().split()))
 
s = sum(a)
target = s//3
count = 0

if n >= 3 and s%3==0:
    sum = 0
    t = 0

    for i in range(n-1):
        sum += a[i]
        if sum == 2*target: count += t
        if sum == target: t+=1
    
print(count)