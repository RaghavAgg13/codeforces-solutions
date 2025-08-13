for j in range(int(input())):
    n, k, x = map(int, input().split())

    if x != 1:
        print("YES")
        print(n)
        print(*[1] * n)
    else:
        if k == 1:
            print("NO")
        elif k >= 2:
            if n % 2 == 0:
                print("YES")
                print(n // 2)
                print(*[2] * (n // 2))
            elif k >= 3:
                print("YES")
                print(n // 2)
                print(3, *[2] * ((n - 3) // 2))
            else:
                print("NO")