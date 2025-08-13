for i in range(int(input())):
    n = int(input())
    s = input()

    posx = posy = 0
    b = False

    for i in s:
        if i == 'U':
            posy += 1
        elif i == 'D':
            posy -= 1
        elif i == 'R':
            posx += 1
        elif i == 'L':
            posx -= 1
        
        if posx == posy == 1:
            b = True
            break

    if posx == posy == 1: b = True

    print('YES' if b else 'NO')