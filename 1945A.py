for i in range(int(input())):
    a,b,c = list(map(int, input().split()))

    if b%3 != 0 and c < 3-b%3:
        print(-1)
    else:
        c = c+b%3
        print(a+b//3+c//3+bool(c%3))