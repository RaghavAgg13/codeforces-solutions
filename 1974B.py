for i in range(int(input())):
    n = int(input())
    a = list(input())
    s = sorted(set(a))

    b = [s[-s.index(i)-1] for i in a]
    print(*b, sep='')