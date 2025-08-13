for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    m1 = min(a)
    m2 = min(b)
    moves = 0
    for i in range(n):
        a[i] -= m1
        b[i] -= m2

        moves += (max(a[i], b[i]))

    print(moves)