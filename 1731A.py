for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    prod = 1
    for i in a: prod *= i
    print(2022*(prod + (n-1)))