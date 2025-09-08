for i in range(int(input())):
    s = input()

    n = 0
    for i in set(s):
        n += 1
        if s.count(i) > 1: n += 1

    print(n//2)