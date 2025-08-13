for i in range(int(input())):
    a = input()
    for i in range(len(a)):
        if a[-1-i] == 'p':
            print('q', end='')
        elif a[-1-i] == 'q':
            print('p', end='')
        else: print(a[-1-i], end='')
    print()