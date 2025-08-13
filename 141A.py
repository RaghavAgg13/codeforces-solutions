s1 = list(input())
s2 = list(input())
s3 = list(input())
b = False

s_check = s1+s2
for i in s_check:
    if i in s3:
        b = True
        s3.remove(i)
    else:
        b = False
        break

if b and len(s3) == 0: print('YES')
else: print('NO')