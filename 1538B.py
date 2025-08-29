for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    count = sum([1 for i in a if i>s//n])

    if s%n != 0:
        print(-1)
    else:
        print(count)