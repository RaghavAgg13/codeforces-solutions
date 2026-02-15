s = str(input())

if '0' not in s:
    print(s[1:])
else:
    s = s.replace('0', '', 1)
    print(s)