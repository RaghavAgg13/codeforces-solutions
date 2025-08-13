for i in range(int(input())):
    n = int(input())
    s = input()
    letters = []
    b = True

    for i in s:
        if i not in letters:
            letters.append(i)
        elif letters[-1] != i:
            b = False
        
    print('YES' if b else 'NO')