for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    idx = 0
    for i in range(n):
        if a[i] > 0:
            idx = i-1
            break

    print(abs(sum(a[idx+1:])+sum(a[:idx+1])))