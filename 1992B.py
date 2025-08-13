for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())), reverse=True)[1:]

    count = a.count(1)
    if 1 in a: a = a[:a.index(1) if 1 in a else -1]
    count += sum(a)*2-(len(a))
    print(count)