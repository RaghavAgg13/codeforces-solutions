for i in range(int(input())):
    a, b = map(int, input().split())

    if a == b:
        print("0 0")
    else:
        diff = abs(a - b)
        
        min_moves = min(a % diff, diff - (a % diff))
        print(diff, min_moves)