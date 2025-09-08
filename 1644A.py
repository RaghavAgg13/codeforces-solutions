for i in range(int(input())):
    a = input()
    if a.index('r') < a.index('R') and a.index('g') < a.index('G') and a.index('b') < a.index('B'):
        print('YES')
    else: print('NO')