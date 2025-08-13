for i in range(int(input())):
    n = input()

    min = 9
    for i in n:
        if int(i) < min: min = int(i)
        if min == 0:
            break

    print(min)