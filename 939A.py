n = int(input())
a = list(map(int, input().split()))

check = False
for i in range(n):
    if a[a[a[i]-1]-1] == i+1:
        check = True
        break

print('YES' if check else 'NO')