for i in range(int(input())):
    a1,a2,b1,b2 = list(map(int, input().split()))
    a = [a1, a2]
    b = [b1, b2]

    final = 0
    for i in range(2):
        for j in range(2):
            count = 0
            if a[i] > b[j]: count += 1
            elif a[i] < b[j]: count -= 1

            if a[1-i] > b[1-j]: count += 1
            elif a[1-i] < b[1-j]: count -= 1

            if count > 0:
                final += 1
    print(final)