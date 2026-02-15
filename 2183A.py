for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if min(a) == 1:
        print("Alice")
    else:
        if a[0] == 1 or a[-1] == 1:
            print("Alice")
        else:
            print("Bob")