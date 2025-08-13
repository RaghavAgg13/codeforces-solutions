for i in range(int(input())):
    s = input()
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')

    print('YES' if a+c==b else 'NO')