for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sum([1 for i in range(n) if a[i] == i+1])

    print(b//2+bool(b%2))