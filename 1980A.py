for i in range(int(input())):
    n,m = list(map(int, input().split()))
    s = sorted(list(input()))

    count = 0
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        if i not in s:
            count += m
        else:
            if s.count(i) < m:
                count += m-s.count(i)

    print(count)