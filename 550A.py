s = input()
n = len(s)
b = False

if n >= 4 and s.count('A') >= 2 and s.count('B') >= 2 and 'AB' in s and 'BA' in s:
    for i in range(n-1):
        if (s[i:i+2] == 'AB' and ('BA' in s[:i] or 'BA' in s[i+2:])) or (s[i:i+2] == 'BA' and ('AB' in s[:i] or 'AB' in s[i+2:])):
            b = True
            break

print('YES' if b else 'NO')