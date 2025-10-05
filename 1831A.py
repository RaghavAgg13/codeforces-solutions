for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(*[n-i+1 for i in a])