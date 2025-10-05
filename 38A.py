n = int(input())
a = list(map(int, input().split()))
x,y = list(map(int, input().split()))

sum = 0
for i in range(x-1, y-1):
    sum += a[i]
print(sum)