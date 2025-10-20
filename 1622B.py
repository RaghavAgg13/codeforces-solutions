for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()

    freq = s.count('1')
    possible = []
    swap = []
    for i in range(n):
        if s[i] == '0':
            if a[i] >= n-freq+1:
                possible.append([a[i], i])
        else:
            if a[i] < n-freq+1:
                swap.append([a[i], i])

    sorted(swap)
    sorted(possible)

    for i in range(len(swap)):
        a[swap[i][1]],a[possible[i][1]] = possible[i][0], swap[i][0]

    print(*a)