for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in set(a):
        count = max(count, a.count(i))

    print(count)