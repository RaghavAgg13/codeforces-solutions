s, t = input(), input()
b = False
if len(s) == len(t):
        for i in range(len(s)):
            if s[i] == t[-(i+1)]:
                b=True
            else:
                b=False
                break
else:
     b=False
if b == True:
    print('YES')
else:
    print('NO')