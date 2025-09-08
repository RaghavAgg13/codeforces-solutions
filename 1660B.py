for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    if (n == 1 and sum(a) == 1) or (n > 1 and abs(a[0]-a[1]) <= 1):
        print('yes')
    else: print('no')