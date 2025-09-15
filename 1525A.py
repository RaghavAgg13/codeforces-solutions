for i in range(int(input())):
    k = int(input())

    a = 1
    b = 0
    while abs(a/(a+b)*100 - k) > 0.000005:
        if a/(a+b)*100 < k:
            a += 1
        elif a/(a+b)*100 > k:
            b += 1
        else: break

    print(a+b)
    