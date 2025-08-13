s = input()
if s.isupper() or s[1:].isupper() or len(s) == 1:
    print(s.swapcase())
else:
    print(s)