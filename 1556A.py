for _ in range(int(input())):
    a,b = list(map(int, input().split()))

    if (a%2 != b%2):
        print(-1)
    elif (a+b == 0):
        print(0)
    elif a != b:
        print(2)
    else:
        print(1)