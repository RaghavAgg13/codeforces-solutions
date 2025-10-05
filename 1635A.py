for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    final = 0
    for i in a: final |= i
    print(final)