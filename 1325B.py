for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = len(set(a))
    print(m)