for i in range(int(input())):
    n = int(input())
    a = input()

    sum = 0
    for i in range(n-1):
        if a[i] != '0':
            sum += int(a[i])
            sum += 1
    sum += int(a[n-1])
    print(sum)