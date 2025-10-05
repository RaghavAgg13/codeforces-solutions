n = int(input())
a = list(map(int, input().split()))
a.sort()

m = min(a)
while m in a: a.remove(m)
print(a[0] if a != [] else 'NO')