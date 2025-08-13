a1 = input()
a2 = input()
f = ''
for i in range(len(a1)):
    if a1[i] == a2[i]:
        f +=  '0'
    else:
        f += '1'
print(f)