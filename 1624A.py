for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    count = 0

    while len(list(set(s))) != 1:
        # print(s)

        max_no = max(s)
        while max_no in s:
            s.remove(max_no)

        max_no_2 = max(s)
        count += max_no - max_no_2

    print(count) 