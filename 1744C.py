for i in range(int(input())):
    n,c = list(map(str, input().split()))
    n = int(n)
    a = input()
    a*=2

    if c == 'g':
        print(0)
        continue

    posOfG = []

    for i,ch in enumerate(a):
        if ch == 'g': posOfG.append(i)


    count = 0
    nextIdx = 0

    for i in range(n):
        if a[i] == c:
            while posOfG[nextIdx] <= i:
                nextIdx += 1
            count = max(count, posOfG[nextIdx] - i)

    print(count)