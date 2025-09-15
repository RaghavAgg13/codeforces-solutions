for i in range(int(input())):
    n = input()

    if '0' in n and '1' in n:
        if len(n)-n[::-1].index('0')-n.index('0') == n.count('0'):
            print(1)
        else: print(2)

    elif '0' in n and '1' not in n:
        print(1)
    elif '0' not in n:
        print(0)