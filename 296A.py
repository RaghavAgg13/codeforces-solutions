n = int(input())
a = list(map(int, input().split()))

check = True
for i in set(a):
    if a.count(i) > n//2+n%2:
        check = False
        break

print('YES' if check or n == 1 else 'NO')