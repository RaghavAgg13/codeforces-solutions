for i in range(int(input())):
    n = int(input())

    print(2)
    if n == 2:
        print("1 2")
    else:
        print(n-2, n)
        print(n-1, n-1)
        for i in range(1, n-2):
            print(n-2-i, n-i)