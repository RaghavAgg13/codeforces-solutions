for i in range(int(input())):
    n,m,r,c = list(map(int, input().split()))

    a = []
    check = 0
    for i in range(n):
        a.append(input())
        if i == r-1 and 'B' in a[i]: check = 1
        elif a[i][c-1] == 'B': check = 1

    if 'B' not in ''.join(a):
        print(-1)
    else:
        if a[r-1][c-1] == 'B': print(0)
        else: print(1 if check else 2)