from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input().strip()
    a = list(map(int, input().split()))

    ops = [1 if c == "A" else 0 for c in s]

    for i in range(q):
        moves = 0
        idx = 0
        score = a[i]

        if 'B' not in s:
            moves = score
            score = 0
        if 'A' not in s:
            moves = score.bit_length()
            score = 0

        while score:
            if idx == n: idx = 0
            if ops[idx]:
                score -= 1
            else:
                score >>= 1
            moves += 1
            idx += 1

        print(moves)
