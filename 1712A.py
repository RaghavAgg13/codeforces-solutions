for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = sorted(a)[:k]
    a = sorted(a[:k])

    final = sum([1 for i in range(k) if a[i] in b])
    print(k-final)