s = input()
b=False
for i in s:
    if i in ['H', 'Q', '9']:
        b=True
if b == True: print('YES')
else: print('NO')