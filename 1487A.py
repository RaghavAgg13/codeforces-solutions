for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = sum([1 for i in range(n) if a[i] > min(a)])
    print(count)