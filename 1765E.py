for i in range(int(input())):
    n,a,b = list(map(int, input().split()))

    if a > b: print(1)
    else:
        print(n//a+bool(n%a))