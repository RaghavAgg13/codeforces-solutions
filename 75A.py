a = input()
b = input()

sum = str(int(a)+int(b))
while '0' in a: a = a.replace('0', "")
while '0' in b: b = b.replace('0', "")
while '0' in sum: sum = sum.replace('0', "")


s = str(int(a)+int(b))

print('YES' if s == sum else 'NO')