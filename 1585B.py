for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    m = a[-1]
    for i in range(n-1, -1, -1):
        if a[i] > m: 
            m = a[i]
            count += 1

    print(count)