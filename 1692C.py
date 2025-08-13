for i in range(int(input())):
    input()
    board = [list(input().strip()) for i in range(8)]
    
    for r in range(1, 7):
        for c in range(1, 7):
            if board[r][c] == "#":
                if (board[r-1][c-1] == "#" and board[r-1][c+1] == "#" and
                    board[r+1][c-1] == "#" and board[r+1][c+1] == "#"):
                    print(r+1, c+1)
                    break
        else:
            continue
        break