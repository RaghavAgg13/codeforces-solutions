for _ in range(int(input())):
    n = int(input())

    arr = []
    fail = False
    while n != 1:
        if n%2 == 0:
            fail = True
            break

        a,b = (n-1)//2, (n+1)//2
        if (a%2 == 0):
            if (b%2 == 0):
                fail = True
                break
            else:
                n = b
                arr.append(1)
        else:
            n = a
            arr.append(2)

    if fail:
        print(-1)
    else:
        print(len(arr))
        print(*arr[::-1])