for i in range(int(input())):
    n,m,k = list(map(int, input().split()))

    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    count = 0

    for i in b:
        for j in c:
            if i+j <= k: count += 1

    print(count)