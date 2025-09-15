for i in range(int(input())):
    n,m = list(map(int, input().split()))

    x,y = 0,0
    count = 0
    for i in range(n):
        a,b = list(map(int, input().split()))

        d = a-x
        parity = 1 if y != b else 0

        if d % 2 == parity:
            count += d
        else:
            count += d - 1

        x,y = a,b

    count += m-x

    print(count)