for i in range(int(input())):
    n,m = list(map(int, input().split()))
    letters = []
    for i in range(n):
        letters.append(input())

    count = 0
    check = 0
    target = 'vika'

    while count < m and check < 4:
        w = [letters[i][count] for i in range(n)]
        if target[check] in w:
            check += 1
        count += 1
    
    if check == 4:
        print('YES')
    else:
        print('NO')