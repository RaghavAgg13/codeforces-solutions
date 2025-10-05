for i in range(int(input())):
    n = int(input())

    moves = 0
    while not n%5:
        n //= 5
        moves += 3

    while not n%3:
        n //= 3
        moves += 2

    while not n%2:
        n /= 2
        moves += 1

    if n == 1: print(moves)
    else: print(-1)