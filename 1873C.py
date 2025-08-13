for i in range(int(input())):
    score = 0
    for i in range(1, 10+1):
        s = input()
        for j in range(1, 10+1):
            if (i in [1, 10] and 1 <= j <= 10 and s[j-1] == 'X') or (2 <= i <= 9 and j in [1, 10] and s[j-1] == 'X'):
                score += 1
            elif (i in [2, 9] and 2 <= j <= 9 and s[j-1] == 'X') or (3 <= i <= 8 and j in [2, 9] and s[j-1] == 'X'):
                score += 2
            elif (i in [3, 8] and 3 <= j <= 8 and s[j-1] == 'X') or (4 <= i <= 7 and j in [3, 8] and s[j-1] == 'X'):
                score += 3
            elif (i in [4, 7] and 4 <= j <= 7 and s[j-1] == 'X') or (5 <= i <= 6 and j in [4, 7] and s[j-1] == 'X'):
                score += 4
            elif (i in [5, 6] and 5 <= j <= 6 and s[j-1] == 'X') or (6 <= i <= 5 and j in [5, 6] and s[j-1] == 'X'):
                score += 5
            # else: score += 5

    print(score)