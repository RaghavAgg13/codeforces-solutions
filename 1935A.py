for i in range(int(input())):
    n = int(input())
    a = input()

    if n%2:
        if a != min(a, a[::-1]):
            print(a[::-1])
        else:
            print(a+a[::-1])
    else:
        if a != min(a, a[::-1]):
            print(a[::-1]+a)
        else:
            print(a)