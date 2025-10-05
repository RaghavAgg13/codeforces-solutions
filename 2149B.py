for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    diff_max = 0
    for i in range(0, n, 2):
        diff_max = max(diff_max, abs(a[i]-a[i+1]))
    print(diff_max)