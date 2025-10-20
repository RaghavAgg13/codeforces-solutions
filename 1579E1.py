from collections import deque
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = deque([a[0]])
    cur_min = a[0]
    for i in range(1, n):
        if a[i] < cur_min:
            b.appendleft(a[i])
            cur_min = a[i]
        else:
            b.append(a[i])

    print(*b)