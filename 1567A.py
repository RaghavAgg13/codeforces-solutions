for i in range(int(input())):
    n = int(input())
    a = input()

    for i in a:
        if i == 'U': print('D', end='')
        elif i == 'D': print('U', end='')
        else: print(i, end='')
    print()