for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = sum([1 for i in a if i%2])

    print(min(count, n-count))