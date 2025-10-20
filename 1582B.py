for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(a.count(1)*(2**a.count(0)))