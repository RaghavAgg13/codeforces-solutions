for i in range(int(input())):
    n,j,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    if (k == 1 and a[j-1] == max(a)) or k != 1: print('YES')
    else: print('NO')