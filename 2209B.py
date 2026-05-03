for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        cnt = 0
        _ = 0
        for j in range(i+1, n):
            if a[i] < a[j]: cnt += 1
            if a[i] > a[j]: _ += 1

        print(max(_, cnt), end = ' ')
    print()