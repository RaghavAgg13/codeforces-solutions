for i in range(int(input())):
    n = input()

    count = 1
    for i in n:
        if int(i) > 1:
            count = max(count, int(i))

    print(count)