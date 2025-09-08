for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = list(set(a))
    for i in b:
        if a.count(i) == 1:
            print(a.index(i)+1)
            break