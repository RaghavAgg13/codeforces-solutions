for i in range(int(input())):
    n = int(input())

    if n%2050:
        print(-1)
    else:
        count = 0
        a = n//2050
        while a > 1:
            count += a%10
            a //= 10
        count += a

        print(count)


