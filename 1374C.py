for i in range(int(input())):
    n = int(input())
    s = input()

    while '()' in s:
        s = s[:s.index('()')] + s[s.index('()')+2:]

    print(len(s)//2)