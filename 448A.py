from math import ceil
a,b,c = list(map(int, input().split()))
sum = ceil((a+b+c)/5)
a,b,c = list(map(int, input().split()))
sum += ceil((a+b+c)/10)

k = int(input())
print('YES' if sum <= k else 'NO')