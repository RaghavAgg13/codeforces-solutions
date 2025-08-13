n = input()
org = n
for i in n:
    x = int(i)
    if x >= 5:
        n = n[:n.index(i)] + str(9-x) + n[n.index(i)+1:]
if n[0] != '0':
    print(n)
else:
    print(org[0] + n[1:])