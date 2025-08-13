for i in range(int(input())):
    for i in range(3):

        s = input()
        for i in s:
            if i == '?':
                if 'A' not in s:
                    print('A')
                elif 'B' not in s:
                    print('B')
                elif 'C' not in s:
                    print('C')