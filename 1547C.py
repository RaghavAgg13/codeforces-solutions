for i in range(int(input())):
    input()
    k,n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    moves = [0]*(m+n)
    i,j = 0,0
    check = True
    for pos in range(m+n):
        if i < n and a[i] == 0:
            moves[pos] = 0
            i += 1
            k += 1
        elif j < m and b[j] == 0:
            moves[pos] = 0
            j += 1
            k += 1
        elif i < n and a[i] <= k:
            moves[pos] = a[i]
            i += 1
        elif j < m and b[j] <= k:
            moves[pos] = b[j]
            j += 1
        else:
            check = False
            break


    if check:
        print(*moves)
    else:
        print(-1)