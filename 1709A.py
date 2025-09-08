for i in range(int(input())):
    x = int(input())
    a = list(map(int, input().split()))

    if a.index(0)+1 == x or (a[a.index(x-1)-1] == 0) or a[0] == 1 or a[1] == 2 or a[2] == 3: 
        print('NO')
    else: print('YES')