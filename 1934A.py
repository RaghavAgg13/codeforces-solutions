for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    print(abs(a[0]-a[-1])+abs(a[-1]-a[1])+abs(a[1]-a[-2])+abs(a[-2]-a[0]))