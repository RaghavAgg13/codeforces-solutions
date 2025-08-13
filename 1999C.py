for i in range(int(input())):
    n,s,m = list(map(int, input().split()))

    b = False
    slots = []
    for i in range(n): slots.append(list(map(int, input().split())))

    if slots[0][0] >= s or (m-slots[-1][-1]) >= s: b = True
    for i in range(1, n):
        if slots[i][0]-slots[i-1][-1] >= s: b = True

    print('YES' if b else 'NO')