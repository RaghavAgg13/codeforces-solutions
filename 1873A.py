t = int(input())

for i in range(t):
    s = input()

    if s in ['abc', 'cba', 'bac', 'acb']:
        print('YES')
    else: # cab, bca
        print('NO')

