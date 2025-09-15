for i in range(int(input())):
    a = input()

    a = list(a)
    a.sort(reverse=True)
    print(*a, sep='')
    # while 'FFT' in a or 'NTT' in a:
    #     for j in ['FFT', 'NTT']:
    #         while j in a:
    #             idx = a.index(j)
    #             a = a[:idx]+j[::-1]+a[idx+3:]

    # print(a)