for i in range(int(input())):
    n = int(input())
    a = list(input())

    b = "".join(sorted(a))
    count = sum([1 for i in range(n) if a[i] != b[i]])
    print(count)