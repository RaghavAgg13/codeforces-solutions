s = input()
b = False
if len(s) >= 7:
    for i in range(len(s)-6):
        if s[i:i+7] in ['1111111', '0000000']:
            b = True

if b == True:
    print('YES')
else:
    print('NO')