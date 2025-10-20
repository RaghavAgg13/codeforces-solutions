for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print(0)
    elif a[-1] == min(a) and a[0] == max(a):
        print(3)
    elif a[0] == min(a) or a[-1] == max(a):
        print(1)
    else: print(2)