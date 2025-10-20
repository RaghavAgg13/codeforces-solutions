for i in range(int(input())):
    n = int(input())
    a = input()

    if '10' in a or '01' in a or '00' in a or a == '0':
        print('YES')
    else:
        print('NO')