n = int(input())
a = list(map(int, input().split()))

cnt = 0
pos = []
b = [i+1 for i in range(n)]

if a == b:
    print(0, 0)
else:

    for i in range(n):
        if a[i] != i+1:
            cnt += 1
            pos.append(i)
            break

    for i in range(n-1, -1, -1):
        if a[i] != i+1:
            cnt += 1
            pos.append(i)
            break

    z = a[:pos[0]]+a[pos[0]:pos[1]+1][::-1]+a[pos[1]+1:]

    if z == b: print(pos[0]+1, pos[1]+1)
    else: print(0, 0)