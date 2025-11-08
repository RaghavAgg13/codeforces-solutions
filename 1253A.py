for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = [0]*(n+2)
    for i in range(1, n+1):
        diff[i] = b[i-1]-a[i-1]

    switch = 0
    element = diff[0]
    for i in range(1, len(diff)):
        if diff[i] != diff[i-1]:
            switch += 1
            if not element: element = diff[i] if diff[i] != 0 else diff[i-1]

    # print(diff, element, switch)
    print('YES' if switch <= 2 and element >= 0 else 'NO')