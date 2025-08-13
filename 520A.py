n = int(input())
s = input().lower()
l1 = []
alphabets = list(map(chr, range(97, 123)))
for i in range(n):
    l1.append(s[i])
l2 = sorted(list(dict.fromkeys(l1)))

if all(item in l2 for item in alphabets):
    print('YES')
else:
    print('NO')