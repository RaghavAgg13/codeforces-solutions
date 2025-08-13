n = int(input())
b = list(map(int, input().split()))

max = max(b)
min = min(b)

n1 = max - min
n2 = b.count(max)*b.count(min) if max != min else n*(n-1)//2
print(n1, n2)