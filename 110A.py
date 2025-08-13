n = input()
count = 0

for i in range(len(n)):
    if n[i] in ['4', '7']:
        count +=1

if count in [4, 7]:
    print('YES')
else: print('NO')