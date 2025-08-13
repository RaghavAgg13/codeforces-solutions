for i in range(int(input())):
    s = ''
    for i in range(1, 8+1):
        l = list(input())
        for i in l:
            if i != '.':
                s += i

    print(s)