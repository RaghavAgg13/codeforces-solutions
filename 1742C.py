for i in range(int(input())):

    b = False
    for i in range(8):
        a = input()
        while a == '': a = input()
        if a == 'R'*8:
            b = True

    print('R' if b else 'B')