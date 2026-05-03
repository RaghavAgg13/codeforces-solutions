for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a != sorted(a):
        a = [1]

    print(len(a))