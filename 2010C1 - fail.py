a = input()
n = len(a)

check = False
for i in range(n//2, n):
    # print(a[i:], '>', a[2*i-n:i])
    if a[i:] == a[2*i-n:i] and i > 0:
        check = True
        print('YES')
        print(a[:i])
        break

if not check: print('NO')