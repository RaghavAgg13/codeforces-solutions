for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if (len(set(a))) != len(a):
        print(-1)
    else:
        print(*sorted(a, reverse=True))