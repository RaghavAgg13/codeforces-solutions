for i in range(int(input())):
    n = int(input())
    a = str(input())

    if a[:4] == '2020' or a[-4:] == '2020':
        print('YES')
    elif a[0] == '2' and a[-3:] == '020':
        print('YES')
    elif a[:2] == '20' and a[-2:] == '20':
        print('YES')
    elif a[:3] == '202' and a[-1] == '0':
        print('YES')
    else: print('NO')