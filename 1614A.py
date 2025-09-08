for i in range(int(input())):
    n,l,r,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = []
    for i in a:
        if l <= i <= r:
            b.append(i)

    b.sort()
    count = 0
    sum = 0
    for i in b:
        if sum+i <= k:
            count += 1
            sum += i
        else:
            break

    print(count)