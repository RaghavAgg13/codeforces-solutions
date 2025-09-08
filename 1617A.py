for i in range(int(input())):
    s = input()
    a = input()

    s = sorted(s)

    if a == 'abc' and 'a' in s and 'b' in s and 'c' in s:
        for i in 'acb':
            print(i*s.count(i), end='')
        for j in s:
            if j not in ['a', 'b', 'c']: print(j, end='')
        print()

    else:
        print(*s, sep='')