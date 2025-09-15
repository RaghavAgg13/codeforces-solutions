for i in range(int(input())):
    a = input()
    n = len(a)

    min = 'z'
    idx = n-1
    for i in range(n):
        if a[i] <= min:
            min = a[i]
            idx = i


    print(a[idx], a[:idx]+a[idx+1:])
