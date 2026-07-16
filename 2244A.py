for _ in range(int(input())):
    n = int(input())
    s = input()

    max_len, len = 0,0
    for i in range(n):
        if s[i] == '#':
            len += 1
        else:
            max_len = max(max_len, len)
            len = 0
    
    max_len = max(max_len, len)
    print((max_len+1)//2)
    