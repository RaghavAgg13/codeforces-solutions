n = int(input())
a = list(map(int, input().split()))
b = []
while a != []:
    if a.count(a[0]) == 1: b.append(a[0])
    a.remove(a[0])


print(len(b))
print(*b)