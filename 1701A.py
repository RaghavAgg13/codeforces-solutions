for i in range(int(input())):
    a = list(map(int, input().split()))
    a += list(map(int, input().split()))

    if a.count(1) == 0:
        print(0)
    elif a.count(1) <= 3:
        print(1)
    else:
        print(2)