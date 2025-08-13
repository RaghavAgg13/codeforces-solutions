for i in range(int(input())):
    l = input()

    b = False
    while '10' in l or '01' in l:
        if '10' in l:
            idx = l.index('10')
            l = l[:idx] + l[idx+2:]
            b = not b

        if '01' in l:
            idx = l.index('01')
            l = l[:idx] + l[idx+2:]
            b = not b

    print('DA' if b else 'NET')