t = int(input())

for i in range(t):
    s = input()

    if len(s)%2 == 0:
        if s[:int(len(s)/2)] == s[int(len(s)/2):]:
            print('YES')
        else: print('NO')
    else: print('NO')