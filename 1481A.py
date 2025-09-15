for i in range(int(input())):
    x,y = list(map(int, input().split()))
    a = input()

    if -a.count('L') <= x <= a.count('R') and -a.count('D') <= y <= a.count('U'):
        print('YES')
    else: print('NO')