for i in range(int(input())):
    n = int(input())
    a = input()

    count = 0
    for i in range(n-1, -1, -1):
        if a[i] == 'B':
            if 'A' in a[:i]:
                count = i-a.index('A')
            break

    print(count)