n = int(input())
l = sorted(list(map(int, input().split())))
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))


if l[:-1] != a:
    for i in range(n-1):
        if l[i] != a[i]:
            print(l[i])
            break
else:
    print(l[-1])

if a[:-1] != b:
    for i in range(n-2):
        if a[i] != b[i]:
            print(a[i])
            break
else:
    print(a[-1])