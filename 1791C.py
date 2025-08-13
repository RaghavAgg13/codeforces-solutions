for i in range(int(input())):
    n = int(input())
    s = input()

    while (s[0] == '1' and s[-1] == '0') or (s[0] == '0' and s[-1] == '1'):
        s = s[1:-1]
        n -= 2

        if s == '': break
    
    print(n)