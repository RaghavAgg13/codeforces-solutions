for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)

    if s%2:
        print("NO")
    else:
        if s%4  == 0:
            print("YES")
        else:
            print("NO")