n = int(input())
numbers = []
b = False
for i in range(1, 1001):
    if '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '5' not in str(i) and '6' not in str(i) and '8' not in str(i) and '9' not in str(i) and '0' not in str(i):
        numbers.append(i)

for i in numbers:
    if n%i == 0:
        b = True
if b == True: print('YES')
else: print('NO')