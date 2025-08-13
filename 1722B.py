for i in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()

    for i in range(n):
        if (s1[i] in ['B', 'G'] and s2[i] in ['G', 'B']) or (s1[i] == s2[i] == 'R'):
            b = True
        else:
            b = False
            break
    
    print('YES' if b else 'NO')