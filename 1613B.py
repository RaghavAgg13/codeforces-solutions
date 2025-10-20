for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    for i in range(n//2):
        print(a[-i-1], a[0])