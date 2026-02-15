import sys

cnt = 0
final = 0
for line in sys.stdin:
    a = line.strip()

    if not a: break
    if a[0] == "+": cnt += 1
    elif a[0] == "-": cnt -= 1
    else: 
        b = a.split(":")
        final += cnt*len(b[1])

print(final)
